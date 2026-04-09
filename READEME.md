# 🔍 Verificador de Domínios com Selenium

Este projeto é um script de automação em Python que utiliza Selenium para verificar a disponibilidade de domínios no site Registro.br. A aplicação lê uma lista de domínios a partir de um arquivo Excel, realiza as consultas simulando o comportamento de um usuário humano e exporta os resultados para um arquivo de texto.

---

## 📌 Funcionalidades

- Leitura de domínios via arquivo Excel(`xls`)
- Automação de navegação com Selenium
- Simulação de digitação humana
- Verificação de disponibilidade de domínios
- Geração de arquivo com os resultados(`resultado.txt`)

---

## 🚀 Tecnologias utilizadas

- Python
- Selenium
- Pandas

---

## 📂 Estrutura do projeto
- main.py: O código principal da automação.

- excel.xls: Arquivo de entrada contendo os domínios na primeira coluna da "Plan1".

- resultado.txt: Arquivo gerado automaticamente com o status das verificações.

---

## ▶️ Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/GustavoRibeiroLobato/verificador-dominios-registrobr.git
cd verificador-dominios-registrobr
```

### 2. Instalar as dependências
```
pip install -r requirements.txt
```

### 3. Executar o Script
```
python main.py
```

---
## ⚙️ Funcionamento do Script

O script conta com funções modulares para facilitar a manutenção:

1. digitar_como_humano(): Adiciona um atraso entre as teclas para mimetizar um usuário real.
2. iniciar_driver(): Configura o Chrome para iniciar maximizado.
3. ler_excel(): Extrai os dados da planilha usando Pandas.
4. verifica_dominio(): Gerencia a espera explícita (WebDriverWait) e a lógica de identificação de texto na página do Registro.br.

---
## 👨‍💻 Autor

**Gustavo Ribeiro Lobato**

---

## 📄 Licença

Este projeto está sob a licença MIT.