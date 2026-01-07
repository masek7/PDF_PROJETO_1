# Extrator Inteligente de Notas Fiscais (PDF & OCR)

Uma aplicação web de Engenharia de Dados desenvolvida para automatizar a extração de informações financeiras (CNPJ, Data, Valor Total) de notas fiscais.

O sistema utiliza uma abordagem **híbrida**: processa PDFs digitais instantaneamente e aciona um motor de **OCR (Visão Computacional)** automaticamente quando identifica documentos escaneados ou imagens.

## Tecnologias & Stack

* **Core:** Python 3.10+
* **Interface:** Streamlit (Web App)
* **Processamento de PDF:** PyMuPDF (Fitz)
* **OCR & Imagem:** Tesseract-OCR, Pytesseract, Pillow
* **Dados:** Pandas & Regex

## Arquitetura da Solução

Este projeto resolve o problema de qualidade de digitalização comum em empresas:

1.  **Pipeline Híbrido:** O sistema tenta primeiro a extração de texto digital (custo computacional baixo). Se falhar, aciona o Tesseract (custo mais alto), otimizando a performance.
2.  **Tratamento de Imagem (Pre-processing):** Implementação de **Upscaling (Zoom 3.0x)** antes da leitura OCR. Isso permite que o sistema leia notas antigas ou com baixa resolução, corrigindo erros comuns de leitura em caracteres pequenos.
3.  **Feedback de UX:** Interface reativa com indicadores de progresso (`st.spinner`) para gerenciar a expectativa do usuário durante processamentos pesados.

## Funcionalidades (v1.1)

* [x] **Upload em Lote:** Processamento de múltiplos arquivos simultaneamente.
* [x] **OCR Automático:** Leitura de notas escaneadas (fotos/imagens) sem intervenção manual.
* [x] **Extração Inteligente:** Lógica heurística para identificar o **Valor Total** real da nota e a **Data de Emissão**.
* [x] **Editor Interativo:** Tabela `data_editor` para validação humana e correção rápida antes da exportação.
* [x] **Exportação Multi-formato:** Suporte para **CSV** e **Excel (.xlsx)** com formatação financeira nativa.

## Roadmap

* [ ] **Validação de CNPJ:** Algoritmo para verificação matemática dos dígitos verificadores.
* [ ] **Dashboard Analítico:** Gráficos de distribuição de gastos por fornecedor.
* [ ] **Integração via API:** Consulta de status do CNPJ na Receita Federal.
* [ ] **Dockerização:** Criação de container para deploy facilitado em nuvem.

---
