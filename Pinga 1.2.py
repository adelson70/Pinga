import tkinter as tk
from tkinter.font import Font
from tkinter import messagebox
import subprocess
import threading
from os import system
version = '1.2'

# Base de dados dos numeros referentes as unidades
db = {
 '703': 'UBS VERDINHO',
 '704': 'EMEB ANTONIO MINOTTO  ',
 '705': 'AUGUSTO PAVEI',
 '706': 'EMEB HONÓRIO DAL TOE  ',
 '709': 'UBS SANTA LUZIA',
 '710': 'UBS LARANJINHA',
 '711': 'UBS MARIA CÉU',
 '712': 'UBS MINEIRA VELHA',
 '713': 'CARLOS WECKI',
 '715': 'ADOLFO BACK  ',
 '716': 'UBS VILA BELMIRO',
 '717': 'GARDINA MINATTO CECHINEL',
 '718': 'UBS BRASÍLIA',
 '719': 'UBS METROPOL',
 '720': 'FILHO DO MINEIRO  ',
 '721': 'UBS MILANESE',
 '722': 'UBS VILA MANAUS',
 '723': 'VANDETE NUNES LIMA',
 '724': 'UBS SÃO SIMÃO',
 '725': 'JOSÉ FRANCISCO BERTERO',
 '726': 'LINUS JOÃO RECH',
 '727': 'FUNDAÇÃO CULTURAL',
 '728': 'RUBENS ARRUDA RAMOS',
 '729': 'UBS PARAÍSO',
 '730': 'UBS ARGENTINA',
 '731': 'CASEMIRO STACHURSKI',
 '732': 'UBS LINHA BATISTA',
 '733': 'CRAS PROSPERA ',
 '735': 'INTENDENCIA 4°linha',
 '736': 'UBS MINA DO MATO',
 '737': 'JOSÉ ROSO  ',
 '738': 'SANTINA DAGOSTIM SALVADOR',
 '739': 'CAPS INFANTIL',
 '740': 'PROJAE',
 '742': 'ELIZA SAMPAIO ',
 '743': 'CRIANÇA FELIZ  ',
 '744': 'UBS CSU EXTENSÃO',
 '748': 'UBS SANGÃO',
 '749': 'CENTRO DE VIGILÂNCIA EM SAÚDE',
 '750': 'CAPS II ',
 '753': 'CENTRO POP',
 '756': 'UBS SANTA BÁRBARA',
 '757': 'MARIA DE LOURDES CARNEIRO  ',
 '758': 'HERCÍLIO AMANTE  ',
 '759': 'ANTONIO MILANEZ NETTO',
 '760': 'SERAFINA MILIOLI PESCADOR',
 '761': 'UBS OPERÁRIA NOVA',
 '762': 'UBS SANTA AUGUSTA',
 '763': 'UBS ANA MARIA',
 '764': 'CENTRO DE CONTROLE DE ZOONOSES',
 '765': 'UBS RENASCER',
 '766': 'CAETANO RONCHI',
 '767': 'UBS SÃO DEFENDE',
 '768': 'CLOTILDES MARIA MARTINS',
 '769': 'CRAS RENASCER',
 '770': 'UBS SANTO ANTÔNIO',
 '771': 'ACACIO ALFREDO  ',
 '772': 'UBS MÃE LUZIA',
 '773': 'GIÁCOMO BÚRIGO  ',
 '774': 'HERCÍLIO LUZ',
 '775': 'UBS MORRO ESTEVÃO',
 '776': 'MARCILIO DIAS SAN THIAGO',
 '777': 'UBS PRIMEIRA LINHA',
 '778': 'ANTONIO MANGILLI',
 '780': 'CRAS SANTA LUZIA',
 '781': 'CAPS II AD',
 '783': 'UBS PRÓSPERA',
 '784': 'PASCOAL MELLER',
 '785': 'PATIO DE MAQUINAS',
 '786': 'PAULO PATRUZZELIS',
 '788': 'ALMOXARIFADO DA SAÚDE (CENTRAL)',
 '790': 'CRAS TERESA CRISTINA',
 '791': 'BIBLIOTECA MUNICIPAL',
 '792': 'CONSELHO TUTELAR',
 '793': 'FME',
 '794': 'HILDA MELLER  ',
 '795': 'LILI COELHO',
 '796': 'PARQUE NAÇÕES  ',
 '797': 'LUDOVICO COCCOLO',
 '800': 'CEIM MARIO PIZZETI',
 '801': 'OSWALDO HULSE  ',
 '802': 'JORGE DA CUNHA CARNEIRO',
 '803': 'JOSÉ CESÁRIO  ',
 '804': 'JOSÉ CONTIM PORTELLA  ',
 '806': 'INTENDENCIA SANTA LUZIA ',
 '807': 'FIORENTO MELLER',
 '808': 'GIÁCOMO ZANETTE',
 '809': 'JORGE FRYDBERG  ',
 '810': 'DIONIZIO MILLIOLI  ',
 '812': 'DEFESA CIVIL  ',
 '813': 'CENTRAL DE MERENDAS  ',
 '815': 'CASA DO PROFESSOR  ',
 '817': 'AMARO JOÃO BATISTA',
 '819': 'PREFEITURA VELHA  ',
 '820': 'UBS SÃO LUÍS',
 '821': 'UBS PINHEIRINHO',
 '822': 'UBS NOSSA SENHORA DA SALETE',
 '823': 'UBS NOVA ESPERANÇA',
 '824': 'UBS MINA UNIÃO',
 '825': 'UBS MINEIRA NOVA',
 '826': 'CREAS ',
 '828': 'CAPS III',
 '829': '24 HORAS BOA VISTA',
 '830': 'UBALDINA ROCHA GHEDIN',
 '831': 'UBS CRISTO REDENTOR',
 '832': 'UBS COLONIAL',
 '833': 'CRAS CRISTO REDENTOR ',
 '835': 'UBS VILA FRANCESA',
 '836': 'UBS SÃO SEBASTIÃO',
 '837': 'LUIZ LAZZARIN',
 '838': 'ANTONIO COLOMBO  ',
 '839': 'ANGELO DE LUCA  ',
 '840': 'UBS VILA RICA ',
 '842': 'CARLOS GORINI  ',
 '845': 'ÉRICO NONNENMACHER',
 '846': 'JOSÉ GIASSI',
 '847': 'MARIA DA ROSA CUNHA',
 '849': 'MARIA ANGELICA  ',
 '851': 'JAIRO LUIZ  ',
 '852': 'UBS QUARTA LINHA',
 '853': 'CEMJA  ',
 '854': 'CEIM GLAUDINÉIA  ',
 '855': 'CASSEMIRO POTRIKUS',
 '856': 'UBS SÃO MARCOS',
 '857': 'IRIA ZANDÔMENEGO DE LUCA',
 '858': 'CSSA 3',
 '859': 'TANCREDO DE ALMEIDA  ',
 '860': 'UBS MINA DO TOCO',
 '861': 'FORTUNATO BRASIL NASPOLINI',
 '862': 'UBS VILA ZULEIMA',
 '863': 'CRAS VILA MIGUEL  ',
 '864': 'PARQUE ASTRONÔMICO',
 '866': 'VILSON LALAU  ',
 '867': 'UBS CENTRO SOCIAL URBANO',
 '868': 'CEIM DEMBOSKI  ',
 '871': 'USINA ASFALTO  ',
 '872': 'HORTO FLORESTAL ',
 '875': 'ARQUIVO MORTO ',
 '879': 'JUNTA MILITAR ',
 '882': 'PARQUE IMIGRANTES ',
 '883': 'MARECHAL RONDON  ',
 '884': 'FRANCISCO SKRABSKI',
 '885': 'CENTRO DE ESPECIALIDADES ODONTOLOGICAS',
 '886': 'UBS CENTRO',
 '889': 'CSSA 1',
 '890': 'UBS WOSOCRIS/RIO MAINA'
}

# Função para localizar o nome da unidade referente ao número informado pelo usuário
def localidade(numero_bola):
    numero_bola = str(numero_bola)
    loc = db[numero_bola]
    return loc

# Função para limpar a tela
def limpar_console():
    system('cls')

# Função para realizar um ping individual
# Serão três argumentos não nomeados
# ip = numero do ip
# dispositivo = nome do dispositivo
# numero = próprio numero informado pelo usuário
def realizar_ping_individual(ip, dispositivo,numero):
    loc = localidade(numero)

    print(f"Realizando ping em {ip}")

    try:
        subprocess.run(["powershell", "-Command", f"$result = Test-Connection -ComputerName {ip} -Count 2 -ErrorAction Stop; exit !$result.IsSuccessStatusCode"], check=True)
        
        # Mensagem para informar ao usuário que o ping ocorreu com sucesso!
        messagebox.showinfo(f"{dispositivo.upper()} - {loc}", f"Ping bem-sucedido para {dispositivo.upper()} ({ip})")
        limpar_console()

    except subprocess.CalledProcessError:
        limpar_console()

        # Mensagem para informar ao usuário que o ping não ocorreu com sucesso!
        messagebox.showerror(f"{dispositivo.upper()} - {loc}", f"Falha no ping para {dispositivo.upper()} ({ip})")

# Função chamada quando o botão é clicado
# Usado para obter o número de entrada do usuário
def obter_numero(dispositivo):
    try:
        numero = int(entrada_numero.get())
        str_numero = str(numero)

        # Formula para descobrir o segundo octeto do endereçamento IP
        segundo_octeto = numero-700

        # Percorre a base de dados para verificar se o número do usuário é válido
        if str_numero not in db.keys():
            messagebox.showerror(f'NÚMERO NÃO ENCONTRADO',f'O número {numero} não foi localizado na base de dados!')

        # Condição que verifica se o número do usúario é compativel com o limite do segundo octeto do endereço ip
        elif 1 < segundo_octeto <= 255:

            # Dispositivo relogio ponto tera o numero host 150
            if dispositivo == 'Relógio Ponto':
                ip = f'10.{segundo_octeto}.0.150'

            # Dispositivo Telefone VoIP tera o numero host 200
            elif dispositivo == 'Telefone VoIP':
                ip = f'10.{segundo_octeto}.0.200'

            # Dispositivo Alarme tera o numero host 240
            elif dispositivo == 'Alarme':
                ip = f'10.{segundo_octeto}.0.240'

            # Chama a função para realizar o teste de ping para o ip
            realizar_ping_individual(ip,dispositivo,numero)

        # Caso o número informado pelo usuário excede ao limite de endereçamento do octeto
        else:
            messagebox.showerror(f'NÚMERO INVÁLIDO',f'O número {numero} que foi digitado é inválido!')

    except ValueError:
        messagebox.showerror(f'ERRO DE ENTRADA',f'Insira apenas números!')


# Cria a janela principal
janela = tk.Tk()
janela.title(f"Pinga {version}")

# Personalização da font, tamanho e negrito
fonte_personalizada = Font(family="Helvetica", size=11, weight="bold")

# Função para ajustar a largura e altura da janela automaticamente
def ajustar_tamanho_janela():
    janela.update_idletasks()
    largura = janela.winfo_reqwidth()
    altura = janela.winfo_reqheight()    
    janela.geometry(f"{largura+80}x{altura}")

# Função para centralizar a janela na tela do computador
def centralizar_tela():
    largura = 200
    altura = 400

    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    x = (largura_tela - largura) // 2
    y = (altura_tela - altura) // 2

    janela.geometry(f"{largura}x{altura}+{x}+{y}")

# Cria os elementos na janela
tk.Label(janela, text="Insira um numero (ex: 700):", font=fonte_personalizada).pack(pady=10)
entrada_numero = tk.Entry(janela)
entrada_numero.pack(pady=10)

# 3 Botões para fazer o ping no respectivo dispositivo
# Foi usado uma função lambda para chamar a função que obter_numero()
tk.Label(janela, text="Escolha um Dispositivo", font=fonte_personalizada).pack(pady=10)

relogio_ponto = tk.Button(janela, text="Relógio Ponto", command=lambda:obter_numero('Relógio Ponto'))
relogio_ponto.pack(pady=10)

telefone_voip = tk.Button(janela, text="Telefone VoIP", command=lambda:obter_numero('Telefone VoIP'))
telefone_voip.pack(pady=10)

alarme = tk.Button(janela, text="Alarme", command=lambda:obter_numero('Alarme'))
alarme.pack(pady=10)

# Chama a função de centralizar e ajustar a janela
centralizar_tela()
ajustar_tamanho_janela()

# Inicia o loop principal da interface
janela.mainloop()