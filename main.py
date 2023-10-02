from customtkinter import *
import string
from random import sample
from tkinter import messagebox

root = CTk()
root.geometry('400x510')
root.resizable(False, False)
root.title('Gerador de Senhas')
root.iconbitmap('icone.ico')
root.configure(fg_color='#13632B')

frame = CTkFrame(root, width=400, height=100, fg_color='#156E2F')
frame.place(x=0, y=0)

labelfrase = CTkLabel(root, text='Gerador de Senhas', fg_color='#156E2F',
                      font=('Arial', 35, 'bold'), text_color='#FFA878')
labelfrase.place(x=40, y=30)


def gerar_senha():
    # Recebendo a função no valor ativo
    numeros = string.digits
    letras_minu = string.ascii_lowercase
    letras_maiu = string.ascii_uppercase
    simbolos = string.punctuation

    global combinar
    combinar = ''
    senha = ''  # Limpando as senhas geradas

    # Condição para cada opção escolhida
    if estado_numero.get() == numeros:
        combinar = numeros
    else:
        pass
    if estado_letras_minu.get() == letras_minu:
        combinar = combinar + letras_minu
    else:
        pass
    if estado_letras_maiu.get() == letras_maiu:
        combinar = combinar + letras_maiu
    else:
        pass
    if estado_simbolos.get() == simbolos:
        combinar = combinar + simbolos
    else:
        pass

    # Geração da senha
    senha = ''.join(sample(combinar, int(entry_qtd_carac.get())))
    senha_label = CTkLabel(root, width=230, height=40, fg_color='#156E2F',
                           corner_radius=10, font=('Arial', 20, 'bold'),
                           text=f'{str(senha)}')
    senha_label.place(x=40, y=435)

    # Função para copiar a senha
    def copiar_senha():
        senha_copiada = senha       # Variável para pegar a senha
        root.clipboard_clear()      # Limpando a área de transferência.
        root.clipboard_append(senha_copiada)  # Copiando a senha
        messagebox.showinfo(title='Info', message='Senha copiada com sucesso!')

    botao_copiar_senha = CTkButton(root, text='Copiar', width=50,
                                   font=('Arial', 20, 'bold'),
                                   text_color='white', fg_color='#012E57',
                                   hover_color='#013869',
                                   command=copiar_senha)
    botao_copiar_senha.place(x=285, y=439)


entry_qtd_carac = CTkEntry(root, width=50, justify='center',
                           border_color='#FFA878',
                           fg_color='#13632B',
                           font=('Arial', 20, 'bold'))
entry_qtd_carac.place(x=35, y=130)

label_qtd_carac = CTkLabel(root, text='Quantidade de Caracteres',
                           font=('Arial', 20, 'bold'), text_color='#FFA878')
label_qtd_carac.place(x=115, y=130)

# Números
numeros = string.digits
estado_numero = StringVar()
switch_numeros = CTkSwitch(root, text='', onvalue=numeros, fg_color='#737373',
                           progress_color='#012E57', button_color='white',
                           offvalue='Inativo',
                           variable=estado_numero)
switch_numeros.place(x=40, y=180)

label_numeros = CTkLabel(root, text='Números', font=('Arial', 20, 'bold'),
                         text_color='#FFA878')
label_numeros.place(x=115, y=180)

# Letras Minúsculas
letras_minu = string.ascii_lowercase
estado_letras_minu = StringVar()
switch_letras_minu = CTkSwitch(root, text='', onvalue=letras_minu,
                               fg_color='#737373', progress_color='#012E57',
                               button_color='white', offvalue='Inativo',
                               variable=estado_letras_minu)
switch_letras_minu.place(x=40, y=230)

label_letras_minu = CTkLabel(root, text='Letras Minúsculas',
                             font=('Arial', 20, 'bold'), text_color='#FFA878')
label_letras_minu.place(x=115, y=230)

# Letras Maiúsculas
letras_maiu = string.ascii_uppercase
estado_letras_maiu = StringVar()
switch_letras_maiu = CTkSwitch(root,  text='', onvalue=letras_maiu,
                               fg_color='#737373', progress_color='#012E57',
                               button_color='white', offvalue='Inativo',
                               variable=estado_letras_maiu)
switch_letras_maiu.place(x=40, y=280)

label_letras_maiu = CTkLabel(root, text='Letras Maiúsculas',
                             font=('Arial', 20, 'bold'), text_color='#FFA878')
label_letras_maiu.place(x=115, y=280)

# Símbolos
simbolos = string.punctuation
estado_simbolos = StringVar()
switch_simbolos = CTkSwitch(root, text='', onvalue=simbolos,
                            fg_color='#737373', progress_color='#012E57',
                            button_color='white',
                            offvalue='Inativo',
                            variable=estado_simbolos)
switch_simbolos.place(x=40, y=320)

label_simbolos = CTkLabel(root, text='Símbolos', font=('Arial', 20, 'bold'),
                          text_color='#FFA878')
label_simbolos.place(x=115, y=320)

button_gerar_senha = CTkButton(root, text='Gerar Senha', text_color='white',
                               font=('Arial', 20, 'bold'), fg_color='#012E57',
                               hover_color='#013869',
                               command=gerar_senha)
button_gerar_senha.place(x=130, y=380)

root.mainloop()
