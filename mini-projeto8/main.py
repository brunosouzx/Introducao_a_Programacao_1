import tkinter as tk
from tkinter import messagebox, font as tkfont, scrolledtext, ttk
import os
import content

class MarketSimulatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Relações de Mercado")
        self.root.geometry("1200x800")
        self.root.configure(bg='#f0f0f0')

        
        self.fonts = {
            "titulo": tkfont.Font(family="Calibri", size=18, weight="bold"),
            "geral": tkfont.Font(family="Calibri", size=11),
            "label": tkfont.Font(family="Calibri", size=12, weight="bold"), 
            "tabela_header": tkfont.Font(family="Calibri", size=11, weight="bold"),
            "tabela_corpo": tkfont.Font(family="Calibri", size=10),
            "axis": tkfont.Font(family="Calibri", size=9),
        }
        self.colors = {
            "background": "#f0f0f0", "frame": "#ffffff", "text": "#000000",
            "header": "#e1e1e1", "accent": "#0078d7", "grid": "#e1e1e1",
            "salario_bar": "#28a745", "rendimento_bar": "#800080", "conforto_bar": "#0078d7",
        }

        self.simulador = content.Simulador()
        self.leitor = content.Leitor()
        self.mes_atual = 0

        if not self._carregar_dados():
            self.root.destroy()
            return

        self.criar_widgets()
        self.atualizar_visualizacao(desenhar_grafico=False) 

    def _carregar_dados(self):
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            self.arquivos_dir = os.path.join(script_dir, 'arquivos')
            self.pessoas = self.leitor.ler_pessoas(os.path.join(self.arquivos_dir, 'pessoas.txt'))
            self.empresas = self.leitor.ler_empresas(os.path.join(self.arquivos_dir, 'empresas.csv'))
            self.categorias = self.leitor.ler_categorias(os.path.join(self.arquivos_dir, 'categorias.json'))
            return True
        except FileNotFoundError as e:
            messagebox.showerror("Erro de Arquivo", f"Arquivo não encontrado: {e.filename}")
            return False

    def _initial_draw_graphs(self, event=None):
        self._desenhar_graficos(self.canvas_graficos)
        self.canvas_graficos.unbind('<Configure>')

    def criar_widgets(self):
        top_frame = tk.Frame(self.root, bg=self.colors['background'])
        top_frame.pack(fill=tk.X, padx=15, pady=(10, 5))
        tk.Label(top_frame, text="SIMULADOR DE RELAÇÕES DE MERCADO", font=self.fonts['titulo'], bg=self.colors['background'], fg=self.colors['accent']).pack()
        control_frame = tk.Frame(top_frame, bg=self.colors['background'], pady=15)
        control_frame.pack(fill=tk.X)
        tk.Label(control_frame, text="Meses para simular:", font=self.fonts['geral'], bg=self.colors['background']).pack(side=tk.LEFT, padx=(0, 5))
        self.meses_entry = tk.Entry(control_frame, width=15, font=self.fonts['geral'], relief=tk.SOLID, borderwidth=1)
        self.meses_entry.pack(side=tk.LEFT, padx=5)
        self.meses_entry.insert(0, "1")
        tk.Button(control_frame, text="Simular", command=self.rodar_simulacao, font=self.fonts['geral'], relief=tk.FLAT, bg=self.colors['header'], padx=10).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Simular 1 Mês", command=self._simular_um_mes, font=self.fonts['geral'], relief=tk.FLAT, bg=self.colors['header'], padx=10).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Resetar", command=self._resetar_simulacao, font=self.fonts['geral'], relief=tk.FLAT, bg=self.colors['header'], padx=10).pack(side=tk.LEFT, padx=5)
        self.meses_simulados_label = tk.Label(control_frame, text="Meses simulados: 0", font=self.fonts['geral'], bg=self.colors['background'])
        self.meses_simulados_label.pack(side=tk.RIGHT)

        style = ttk.Style()
        style.theme_use('default')
        style.configure("TNotebook", background=self.colors['background'], borderwidth=0)
        style.configure("TNotebook.Tab", background=self.colors['header'], foreground="#555555", padding=[15, 5], font=self.fonts['geral'], borderwidth=0)
        style.map("TNotebook.Tab", background=[("selected", self.colors['accent'])], foreground=[("selected", "#ffffff")])
        
        notebook_frame = tk.Frame(self.root, bg=self.colors['background'])
        notebook_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 15))
        notebook = ttk.Notebook(notebook_frame, style="TNotebook")
        notebook.pack(fill=tk.BOTH, expand=True)

        self.tab_categorias = self._criar_aba_texto(notebook, "Categorias")
        self.canvas_pessoas = self._criar_aba_canvas(notebook, "Pessoas")
        self.canvas_empresas = self._criar_aba_canvas(notebook, "Empresas")
        self.canvas_graficos = self._criar_aba_canvas(notebook, "Gráficos")

        self.canvas_graficos.bind('<Configure>', self._initial_draw_graphs)

    def _criar_aba_canvas(self, notebook, text):
        frame = tk.Frame(notebook, bg=self.colors['frame'], relief=tk.SOLID, borderwidth=1)
        notebook.add(frame, text=text)
        canvas = tk.Canvas(frame, bg=self.colors['frame'], highlightthickness=0)
        v_scroll = tk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
        h_scroll = tk.Scrollbar(frame, orient=tk.HORIZONTAL, command=canvas.xview)
        canvas.configure(yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set)
        v_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        h_scroll.pack(side=tk.BOTTOM, fill=tk.X)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        return canvas
    
    def _criar_aba_texto(self, notebook, text):
        
        frame = tk.Frame(notebook, bg=self.colors['frame'], relief=tk.SOLID, borderwidth=1)
        notebook.add(frame, text=text)

        
        header_label = tk.Label(
            frame,
            text="Divisão da Renda Mensal",
            font=self.fonts['label'],
            bg=self.colors['frame'],     
            fg=self.colors['accent']      
        )
        header_label.pack(pady=(10, 5)) 

        # Área de texto com rolagem
        text_widget = scrolledtext.ScrolledText(
            frame,
            font=self.fonts['tabela_corpo'],
            relief=tk.FLAT,
            wrap=tk.WORD,
            padx=10,
            pady=10,
            bg=self.colors['frame'], 
            fg=self.colors['text']   
        )
        text_widget.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        return text_widget

    def _desenhar_eixo_y(self, canvas, x_pos, y_pos, height, max_value, num_ticks=5, prefix="R$ "):
        for i in range(num_ticks + 1):
            valor = max_value * (i / num_ticks)
            y = y_pos + height - (valor / max_value * height if max_value > 0 else 0)
            canvas.create_line(x_pos, y, x_pos + 2000, y, fill=self.colors['grid'], dash=(2, 4))
            if max_value > 0 and max_value < num_ticks: label = f"{prefix}{valor:.1f}"
            else: label = f"{prefix}{valor:,.0f}"
            canvas.create_text(x_pos - 10, y, text=label, anchor='e', font=self.fonts['axis'])

    def _desenhar_graficos(self, canvas):
        canvas.delete("all")
        if not self.pessoas: return
        canvas_width = canvas.winfo_width()
        x_start, x_padding = 60, 20
        chart_area_width = canvas_width - x_start - x_padding
        if chart_area_width < 1: return
        bar_total_width = chart_area_width / len(self.pessoas)
        bar_width = bar_total_width * 0.8
        y_renda, h_renda = 50, 250
        max_renda = max(content.calc_renda_mensal(p) for p in self.pessoas) or 1
        self._desenhar_eixo_y(canvas, x_start, y_renda, h_renda, max_renda)
        for i, p in enumerate(self.pessoas):
            rendimento = p.patrimonio * 0.005
            salario_h = (p.salario / max_renda) * h_renda if max_renda > 0 else 0
            rendimento_h = (rendimento / max_renda) * h_renda if max_renda > 0 else 0
            bar_x = x_start + i * bar_total_width
            canvas.create_rectangle(bar_x, y_renda + h_renda - salario_h, bar_x + bar_width, y_renda + h_renda, fill=self.colors['salario_bar'], outline="")
            canvas.create_rectangle(bar_x, y_renda + h_renda - rendimento_h, bar_x + bar_width, y_renda + h_renda, fill=self.colors['rendimento_bar'], outline="")
        y_legenda_renda = y_renda + h_renda + 20
        canvas.create_rectangle(x_start, y_legenda_renda, x_start + 15, y_legenda_renda + 15, fill=self.colors['salario_bar'])
        canvas.create_text(x_start + 20, y_legenda_renda + 7.5, text="Salário", anchor='w', font=self.fonts['geral'])
        canvas.create_rectangle(x_start + 100, y_legenda_renda, x_start + 115, y_legenda_renda + 15, fill=self.colors['rendimento_bar'])
        canvas.create_text(x_start + 120, y_legenda_renda + 7.5, text="Rendimentos", anchor='w', font=self.fonts['geral'])
        y_conforto, h_conforto = y_renda + h_renda + 70, 200
        max_conforto = max(p.conforto for p in self.pessoas) if any(p.conforto > 0 for p in self.pessoas) else 1.0
        self._desenhar_eixo_y(canvas, x_start, y_conforto, h_conforto, max_conforto, prefix="")
        for i, p in enumerate(self.pessoas):
            conforto_h = (p.conforto / max_conforto) * h_conforto if max_conforto > 0 else 0
            bar_x = x_start + i * bar_total_width
            canvas.create_rectangle(bar_x, y_conforto + h_conforto - conforto_h, bar_x + bar_width, y_conforto + h_conforto, fill=self.colors['conforto_bar'], outline="")
        y_legenda_conforto = y_conforto + h_conforto + 20
        canvas.create_rectangle(x_start, y_legenda_conforto, x_start + 15, y_legenda_conforto + 15, fill=self.colors['conforto_bar'])
        canvas.create_text(x_start + 20, y_legenda_conforto + 7.5, text="Nível de Conforto", anchor='w', font=self.fonts['geral'])
        canvas.configure(scrollregion=canvas.bbox("all"))

    def _desenhar_tabela(self, canvas, headers, data_rows, col_widths):
        canvas.delete("all")
        row_height = 25; x_pad, y_pad = 5, 5; x, y = x_pad, y_pad
        total_width = sum(col_widths)
        canvas.create_rectangle(0, y, total_width, y+row_height, fill=self.colors['header'], outline=self.colors['header'])
        for i, header in enumerate(headers):
            canvas.create_text(x + 5, y + row_height/2, text=header, font=self.fonts['tabela_header'], fill=self.colors['text'], anchor="w")
            x += col_widths[i]
        y += row_height
        for row_data in data_rows:
            x = x_pad
            canvas.create_line(0, y, total_width, y, fill="#eeeeee")
            for i, item in enumerate(row_data):
                canvas.create_text(x + 5, y + row_height/2, text=str(item), font=self.fonts['tabela_corpo'], fill=self.colors['text'], anchor="w")
                x += col_widths[i]
            y += row_height
        canvas.configure(scrollregion=canvas.bbox("all"))

    def _simular_um_mes(self):
        self.mes_atual += 1
        self.simulador.simular_mercado(self.pessoas, self.empresas, self.categorias)
        self.atualizar_visualizacao()

    def _resetar_simulacao(self):
        if messagebox.askokcancel("Resetar Simulação", "Tem certeza que deseja resetar todos os dados para o estado inicial?"):
            self.mes_atual = 0
            if self._carregar_dados():
                
                self.atualizar_visualizacao(desenhar_grafico=True)
                messagebox.showinfo("Sucesso", "A simulação foi resetada.")
            else:
                messagebox.showerror("Erro", "Não foi possível recarregar os dados para resetar.")

    def rodar_simulacao(self):
        try:
            num_meses = int(self.meses_entry.get())
            if num_meses <= 0: raise ValueError
        except ValueError:
            messagebox.showwarning("Entrada Inválida", "Insira um número inteiro positivo de meses.")
            return
        for _ in range(num_meses):
            self.mes_atual += 1
            self.simulador.simular_mercado(self.pessoas, self.empresas, self.categorias)
        self.atualizar_visualizacao()
    
    def _atualizar_texto_categorias(self):
        self.tab_categorias.config(state=tk.NORMAL)
        self.tab_categorias.delete('1.0', tk.END)
        texto = "Divisão da renda mensal:\n\n"; total = sum(self.categorias.values())
        for cat, perc in self.categorias.items():
            texto += f"{cat.capitalize()}: {perc*100:.1f}%\n"
        texto += f"\nTotal: {total*100:.1f}% da renda mensal"
        self.tab_categorias.insert('1.0', texto)
        self.tab_categorias.config(state=tk.DISABLED)

    def atualizar_visualizacao(self, desenhar_grafico=True):
        self.meses_simulados_label.config(text=f"Meses simulados: {self.mes_atual}")
        self._atualizar_texto_categorias()
        
        headers_p = ["Nome", "Patrimônio", "Salário", "Renda Mensal", "Conforto"]
        widths_p = [250, 150, 150, 150, 100]
        rows_p = [[p.nome, f"R$ {p.patrimonio:,.2f}", f"R$ {p.salario:,.2f}", f"R$ {content.calc_renda_mensal(p):,.2f}", f"{p.conforto:.2f}"] for p in self.pessoas]
        self._desenhar_tabela(self.canvas_pessoas, headers_p, rows_p, widths_p)

        headers_e = ["Categoria", "Nome", "Produto", "Qualidade", "Margem", "Custo", "Preço", "Lucro Total", "Vendas"]
        widths_e = [100, 150, 150, 80, 80, 100, 100, 100, 80]
        rows_e = [[e.categoria, e.nome, e.produto, f"{e.qualidade:.1f}", f"{e.margem*100:.1f}%", f"R$ {e.custo:.2f}", f"R$ {content.calc_preco(e):.2f}", f"R$ {e.vendas * e.custo * e.margem:.2f}", e.vendas] for e in self.empresas]
        self._desenhar_tabela(self.canvas_empresas, headers_e, rows_e, widths_e)
        
        if desenhar_grafico:
            self._desenhar_graficos(self.canvas_graficos)

if __name__ == "__main__":
    root = tk.Tk()
    app = MarketSimulatorApp(root)
    root.mainloop()