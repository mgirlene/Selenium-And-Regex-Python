import PyPDF2
import re
import json


class ExtractInformationsFatura:

    def read_pdf(arquivo):
        pdf_file = open(arquivo, 'rb')
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()

        return page_content

    def extract_infos_regex(texto):
        page_content = texto
        dict_fatura = {}

        regex_nome_pagador = re.compile('Pagador:([A-zÀ-ú ]+)', re.DOTALL)
        dict_fatura["nome_pagador"] = re.search(
            regex_nome_pagador, page_content).group(1)

        regex_numero_cliente = re.compile('MONOFÁSICO([0-9]+)', re.DOTALL)
        dict_fatura["numero_cliente"] = re.search(
            regex_numero_cliente, page_content).group(1)

        regex_cpf = re.compile('CPF/CNPJ: ([0-9\.-]+)', re.DOTALL)
        dict_fatura["cpf_cliente"] = re.search(
            regex_cpf, page_content).group(1)

        regex_cep = re.compile('CEP: ([0-9]+)', re.DOTALL)
        dict_fatura["cep_cliente"] = re.search(
            regex_cep, page_content).group(1)

        regex_cnpj = re.compile('[^CPF/]CNPJ: ([0-9\.-\/]+)', re.DOTALL)
        dict_fatura["cnpj_companhia"] = re.search(
            regex_cnpj, page_content).group(1)

        regex_cgf = re.compile('CGF: ([0-9\.-]+)', re.DOTALL)
        dict_fatura["cgf_companhia"] = re.search(
            regex_cgf, page_content).group(1)

        regex_vencimento = re.compile('([0-9/]+)\nR\$', re.DOTALL)
        dict_fatura["data_vencimento"] = re.search(
            regex_vencimento, page_content).group(1)

        regex_total = re.compile('R\$ ([0-9,.]+)', re.DOTALL)
        dict_fatura["total"] = re.search(regex_total, page_content).group(1)

        regex_dt_emissao = re.compile('DATA DE EMISSÃO: ([0-9/]+)', re.DOTALL)
        dict_fatura["data_emissao"] = re.search(
            regex_dt_emissao, page_content).group(1)

        regex_leitura_anterior = re.compile(
            '([0-9/]+)\n[0-9/]+\n[0-9]+\n[0-9/]+', re.DOTALL)
        dict_fatura["leitura_anterior"] = re.search(
            regex_leitura_anterior, page_content).group(1)

        regex_leitura_atual = re.compile(
            '[0-9/]+\n([0-9/]+)\n[0-9]+\n[0-9/]+', re.DOTALL)
        dict_fatura["leitura_atual"] = re.search(regex_leitura_atual, page_content).group(1)

        return dict_fatura

    def convert_to_json(dict_fatura):
        with open("fatura_energia.json", "w") as data:
            json.dump(dict_fatura, data)


pdf = ExtractInformationsFatura.read_pdf(r'C:\Users\MariaGirlene\Downloads\BILLING_BR_CE_20220506071656_0000000045713828_4562_311249749286.PDF')

dict_fatura = ExtractInformationsFatura.extract_infos_regex(pdf)

ExtractInformationsFatura.convert_to_json(dict_fatura)




