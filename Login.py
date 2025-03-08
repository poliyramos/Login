import customtkinter as ctk

# Aparência
ctk.set_appearance_mode('dark')

# Criação da função
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    # Verificar usuario e senha
    if usuario == 'poliana' and senha == '12345':
        resultado_login.configure(text='Login feito com sucesso!', text_color='green')
    else:
        resultado_login.configure(text='Login incorreto', text_color='red')    
        

# Janela
app = ctk.CTk()
app.title('Login')
app.geometry('300x300')

# Criação dos Campos
# Label
label_usuario = ctk.CTkLabel(app, text='Usuário')
label_usuario.pack(pady=10)
# Entry
campo_usuario = ctk.CTkEntry(app, placeholder_text='Digite seu usuário')
campo_usuario.pack(pady=10)
# Label
label_senha = ctk.CTkLabel(app, text='Senha')
label_senha.pack(pady=10)
# Entry
campo_senha = ctk.CTkEntry(app, placeholder_text='Digite sua senha', show='*')
campo_senha.pack(pady=10)
# Botão
botao_login = ctk.CTkButton(app, text='Login', command=validar_login)
botao_login.pack(pady=10)
# Campo feedback
resultado_login = ctk.CTkLabel(app, text='')
resultado_login.pack(pady=10)



app.mainloop()