import streamlit as st
from datetime import datetime
from reportlab.pdfgen import canvas
from io import BytesIO

# Configuração da página
st.set_page_config(page_title="PIC - FORTNEER", page_icon="🏥", layout="wide")

# Cabeçalho
st.title("PIC - Protocolo de Interpretação e Conduta Médica")
st.subheader("FORTNEER - ASSESSORIA PARA REGULARIZAÇÃO EMPRESARIAL (Sombrio & Morro da Fumaça)")
st.markdown("---")

# Menu lateral
menu = st.sidebar.selectbox("Menu", [
    "Introdução",
    "Aptidão para Atividades Críticas",
    "Exames com Normas Específicas",
    "Afastamento e Restrições",
    "Retorno ao Trabalho",
    "Manipuladores de Alimentos",
    "Doenças Relacionadas ao Trabalho",
    "Avaliações Não Ocupacionais",
    "Avaliação de PCD"
])

# Conteúdo baseado na seleção do menu
if menu == "Introdução":
    st.header("Introdução")
    st.write("""
    A conduta médica para interpretação dos exames e definição de aptidão ao trabalho deve seguir critérios técnico-científicos, éticos e normativos. 
    Este protocolo foi elaborado baseado nos preceitos éticos e na legislação vigente e tem por abrangência todos os atendimentos realizados por médicos em agendamentos feitos pela FORTNEER ou por suas empresas clientes.
    """)
    
    st.subheader("Princípios Gerais")
    st.write("""
    1. Os médicos examinadores devem seguir os critérios deste protocolo, em alinhamento às alíneas 'c' e 'd' do item 7.5.4 da NR-7 e ao § 1º do Art. 5º da Resolução 2323/2022 do CFM.
    2. É facultada a adoção de condutas diferentes das sugeridas, desde que justificadas e registradas no prontuário.
    3. Em caso de dúvidas ou condutas diferentes, o médico deve contatar o responsável pela saúde ocupacional da FORTNEER.
    4. Os trabalhadores devem ser informados sobre os exames e seus resultados (conforme item 7.5.16 da NR-7).
    5. Observar toda a Resolução 2323/2022 do CFM, especialmente Art. 1º, Art. 2º e Art. 4º.
    """)
    
    st.subheader("Responsabilidades")
    st.write("""
    - O médico pode solicitar repetição de exames ou novos exames para formação de convicção técnica.
    - Todas as condutas devem ser justificadas tecnicamente e discutidas com o médico responsável pelo PCMSO.
    """)

elif menu == "Aptidão para Atividades Críticas":
    st.header("Aptidão e Inaptidão para Atividades Críticas")
    st.write("""
    Atividades críticas são definidas na NR-7 como aquelas que exigem avaliação médica específica para definir a aptidão do empregado.
    """)
    
    st.subheader("Exemplos de Atividades Críticas")
    st.write("""
    - Trabalhos com risco significativo de queda de altura
    - Trabalhos em espaços confinados
    - Operações diversas com risco significativo de acidentes
    - Condução habitual e frequente de veículos motorizados
    - Operação de máquinas perigosas
    - Operação constante de pontes rolantes
    - Atividades com risco de choques elétricos de grandes proporções
    - Outras atividades que, a critério médico, exijam avaliação específica
    """)
    
    st.subheader("Critério Tricolor")
    st.write("""
    Sistema de classificação para orientar a conduta médica:
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.success("**Sinal Verde**")
        st.write("Condição que, por si só, não deve ser considerada como critério de incompatibilidade.")
    with col2:
        st.warning("**Sinal Amarelo**")
        st.write("Condição que merece investigação e/ou acompanhamento. O médico deve definir se o trabalhador pode exercer as atividades.")
    with col3:
        st.error("**Sinal Vermelho**")
        st.write("Existe contraindicação para a execução de atividades críticas.")
    
    st.subheader("Avaliações Específicas")
    evaluation = st.selectbox("Selecione a avaliação:", [
        "Acuidade Visual e Avaliação Oftalmológica",
        "Arritmias Cardíacas e ECG",
        "Hipertensão Arterial",
        "Diabetes e Glicemia em Jejum",
        "Obesidade",
        "Anemias e Hemograma",
        "Equilíbrio e Consciência",
        "Fatores Psicossociais",
        "Acuidade Auditiva"
    ])
    
    if evaluation == "Acuidade Visual e Avaliação Oftalmológica":
        st.subheader("Acuidade Visual e Avaliação Oftalmológica")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.success("**Sinal Verde**")
            st.write("""
            - Acuidade Visual ≥ 20/40 em cada olho
            - Acuidade Visual ≥ 20/30 + PL em um dos olhos
            - Visão periférica ≥ 60° em cada olho ou ≥ 120° em um olho
            """)
        with col2:
            st.warning("**Sinal Amarelo**")
            st.write("""
            - Visão monocular com perda visual antiga + visão periférica ≥ 120°
            """)
        with col3:
            st.error("**Sinal Vermelho**")
            st.write("""
            - Visão monocular com perda visual recente
            """)
    
    elif evaluation == "Arritmias Cardíacas e ECG":
        st.subheader("Arritmias Cardíacas e ECG (Eletrocardiograma)")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.success("**Sinal Verde**")
            st.write("""
            - Alterações de repolarização ventricular
            - Extrassístoles atriais isoladas
            - Bradiarritmia sinusal > 45 bpm
            - BAV 1° grau
            - BRD isolado
            - Bloqueio do fascículo anterior-superior E
            - Bloqueio do fascículo postero-inferior
            """)
        with col2:
            st.warning("**Sinal Amarelo**")
            st.write("""
            - Sobrecarga de VE
            - Extrassístoles atriais frequentes
            - Extra-sístoles ventriculares isoladas e frequentes
            - Bradiarritmia sinusal ≤ 45 bpm
            - BAV 2° grau tipo I
            - BRE (avaliação cardiológica rigorosa)
            """)
        with col3:
            st.error("**Sinal Vermelho**")
            st.write("""
            - BAV 2° grau tipo II adquirido
            - BAV total
            - Taquicardia Supraventricular Paroxística
            """)
    
    elif evaluation == "Hipertensão Arterial":
        st.subheader("Hipertensão Arterial")
        
        st.write("""
        **Classificação da pressão arterial (a partir de 18 anos):**
        """)
        
        st.table({
            "Classificação": ["PA ótima", "PA normal", "Pré-hipertensão", "HA Estágio 1", "HA Estágio 2", "HA Estágio 3"],
            "PAS (mmHg)": ["< 120", "120-129", "130-139", "140-159", "160-179", "≥ 180"],
            "PAD (mmHg)": ["< 80", "80-84", "85-89", "90-99", "100-109", "≥ 110"]
        })
        
        st.write("""
        **Fatores de risco coexistentes:**
        - Sexo masculino
        - Idade: > 55 anos (homem), > 65 anos (mulher)
        - DCV prematura em parentes de 1º grau
        - Tabagismo
        - Dislipidemia
        - Diabetes melito
        - Obesidade (IMC ≥ 30 kg/m²)
        """)
        
        st.write("""
        **Classificação de risco:**
        """)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.success("**Sinal Verde**")
            st.write("Indivíduos com risco basal ou baixo risco adicional")
        with col2:
            st.warning("**Sinal Amarelo**")
            st.write("Indivíduos com moderado risco adicional - avaliação cardiológica e relatório")
        with col3:
            st.error("**Sinal Vermelho**")
            st.write("""
            - Indivíduos com alto risco adicional
            - Hipotensão ortostática (redução ≥20 mmHg PAS ou ≥10 mmHg PAD ao 3º minuto em pé)
            """)
    
    elif evaluation == "Diabetes e Glicemia em Jejum":
        st.subheader("Diabetes e Glicemia em Jejum")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.success("**Sinal Verde**")
            st.write("Diabetes mellitus não insulinodependente bem controlado - GJ < 130 mg/dl")
        with col2:
            st.warning("**Sinal Amarelo**")
            st.write("""
            - Diabetes mellitus não insulinodependente mal controlado - GJ > 130 mg/dl
            - Diabéticos com PA>140/90
            """)
        with col3:
            st.error("**Sinal Vermelho**")
            st.write("Diabetes mellitus insulinodependente")
    
    elif evaluation == "Obesidade":
        st.subheader("Obesidade")
        
        st.write("""
        **Classificação pelo IMC (kg/m²):**
        """)
        
        st.table({
            "IMC": ["<18,5", "18,5-24,9", "25-29,9", "30-34,9", "35-39,9", "≥40,0"],
            "Classificação": ["Magro/baixo peso", "Normal/eutrófico", "Sobrepeso/pré-obeso", "Obesidade", "Obesidade", "Obesidade grave"],
            "Grau": ["0", "0", "0", "I", "II", "III"],
            "Risco": ["Normal/elevado", "Normal", "Pouco elevado", "Elevado", "Muito elevado", "Muitíssimo elevado"]
        })
        
        st.write("""
        **Critério tricolor:**
        """)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.success("**Sinal Verde**")
            st.write("Obesidade grau I com IMC > 30 com até 100kg")
        with col2:
            st.warning("**Sinal Amarelo**")
            st.write("""
            - Obesidade Grau I com IMC > 30 com mais de 100kg
            - Obesidade Grau II e III com IMC > 35 com até 100kg
            """)
        with col3:
            st.error("**Sinal Vermelho**")
            st.write("""
            - Obesidade Grau II e III com IMC > 35 com mais de 100kg*
            *Pode ser sinal amarelo ou vermelho a critério médico
            """)
    
    elif evaluation == "Anemias e Hemograma":
        st.subheader("Anemias e Hemograma")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.success("**Sinal Verde**")
            st.write("-")
        with col2:
            st.warning("**Sinal Amarelo**")
            st.write("Anemias com Hb > 8g/dL sem episódios de lipotimia ou síncope")
        with col3:
            st.error("**Sinal Vermelho**")
            st.write("""
            - Anemias com Hb > 8g/dL com episódio de lipotimia ou síncope
            - Anemias com Hb < 8g/dL
            - Anemias hemolíticas, falciforme, talassemia major e outras com crises frequentes
            """)
    
    elif evaluation == "Equilíbrio e Consciência":
        st.subheader("Equilíbrio e Consciência")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.success("**Sinal Verde**")
            st.write("-")
        with col2:
            st.warning("**Sinal Amarelo**")
            st.write("""
            - Síndromes labirínticas
            - Epilepsia em bom controle (sem crises há >1 ano)
            """)
        with col3:
            st.error("**Sinal Vermelho**")
            st.write("""
            - Epilepsia sem controle adequado ou com crise nos últimos 12 meses
            - Síncope com causa cardíaca
            """)
    
    elif evaluation == "Fatores Psicossociais":
        st.subheader("Fatores Psicossociais")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.success("**Sinal Verde**")
            st.write("-")
        with col2:
            st.warning("**Sinal Amarelo**")
            st.write("-")
        with col3:
            st.error("**Sinal Vermelho**")
            st.write("""
            - Acrofobia (pânico de altura)
            - Uso constante de álcool/drogas/medicações que interferem na cognição
            - Alcoolismo
            - Síndrome do pânico
            - Grau de instrução incompatível
            """)
    
    elif evaluation == "Acuidade Auditiva":
        st.subheader("Acuidade Auditiva")
        
        st.write("""
        - Avaliação inicial por prova da voz coloquial (2m de distância, sem leitura labial)
        - Em caso de reprovação, solicitar audiometria tonal aérea
        - Critério de aptidão: média aritmética em 500, 1000 e 2000 Hz <40 dB na orelha melhor
        - Entre 40-56 dB: avaliar necessidade de prótese auditiva
        - Declarar "obrigatório o uso de prótese auditiva" quando aplicável
        """)

elif menu == "Exames com Normas Específicas":
    st.header("Exames com Critérios Definidos em Normas Específicas")
    
    st.write("""
    Alguns exames possuem critérios para interpretação e conduta médica definidos em normas específicas. 
    Nesses casos, prevalece o critério estabelecido pelos órgãos competentes e as normativas vigentes.
    """)
    
    st.subheader("NR-7 - Item 7.5.19.5")
    st.write("""
    Constatada ocorrência ou agravamento de doença relacionada ao trabalho ou alteração que revele disfunção orgânica:
    """)
    
    st.write("""
    1. Emitir a Comunicação de Acidente do Trabalho (CAT)
    2. Afastar o empregado quando necessário
    3. Encaminhar à Previdência Social para afastamentos >15 dias
    4. Reavaliar os riscos ocupacionais e medidas de prevenção no PGR
    """)

elif menu == "Afastamento e Restrições":
    st.header("Afastamento, Restrições e Viabilização de Posto Compatível")
    
    st.write("""
    Os médicos podem prescrever modificações ou restrições nas atividades de trabalho, temporárias ou permanentes, 
    independentemente da origem ocupacional da patologia.
    """)
    
    st.subheader("Procedimentos")
    st.write("""
    1. Avaliar a condição de saúde do trabalhador
    2. Prescrever as restrições e recomendações
    3. Registrar em prontuário médico e documento apartado
    4. Notificar a organização (respeitando sigilo médico)
    """)
    
    st.write("""
    **Base Legal:**
    - Lei 605/1949 (§2º Art.6º)
    - NR-7 (item 7.5.9.1, alíneas "c", "f", "i" e "k" do item 7.3.2)
    - Resolução CFM 2323/2022 (Art.4º)
    """)

elif menu == "Retorno ao Trabalho":
    st.header("Exame Médico de Retorno ao Trabalho")
    
    st.write("""
    Deve ser realizado antes que o empregado reassuma suas funções, quando ausente por ≥30 dias por doença ou acidente 
    (ocupacional ou não).
    """)
    
    st.subheader("Objetivos")
    st.write("""
    - Avaliar regressão do quadro que originou o afastamento
    - Verificar se não houve outros agravos à saúde
    - Definir necessidade de retorno gradativo
    - Propor orientações ou adaptações quando necessário
    """)
    
    st.subheader("Procedimentos")
    st.write("""
    1. Realizar exame clínico antes do retorno
    2. Definir exames complementares conforme PCMSO
    3. Em caso de exames periódicos vencidos, agendar novo exame
    """)
    
    st.subheader("Limbo Trabalhista Previdenciário")
    st.write("""
    Situação em que o trabalhador não recebe pagamentos da empresa nem da Previdência.
    """)
    
    st.write("""
    **Recomendações para evitar o limbo:**
    - Considerar a hierarquia dos atestados (decisão do INSS é soberana)
    - Quando possível, realizar exame 1-2 dias ANTES da DCB (Data de Cessação do Benefício)
    - Tentar viabilizar o retorno, mesmo com restrições
    - Em caso de inaptidão, solicitar prorrogação do benefício
    """)
    
    st.write("""
    **Referências Legais:**
    - Lei 605/1949
    - Súmula 15 do TST
    - Lei 11907/2009 (§3º Art.30)
    - Resolução CFM 2323/2022 (Art.4º e inciso II do Art.3º)
    - NR-7 (itens 7.5.9, 7.5.9.1 e alíneas "f", "j" e "k" do item 7.3.2)
    """)

elif menu == "Manipuladores de Alimentos":
    st.header("Manipuladores de Alimentos")
    
    st.write("""
    Base legal: RDC 216/2004 e 275/2002 da Vigilância Sanitária.
    """)
    
    st.subheader("Aptidão para Manipulação de Alimentos")
    st.write("""
    1. Declarar no ASO ou documento separado a aptidão/inaptidão
    2. Não há obrigatoriedade de exames complementares, exceto se determinado pelo PCMSO ou Vigilância Sanitária local
    3. Considerar critérios da RDC 216/2004 (item 4.6.2) e RDC 275/2002 (Anexo II, item 3.3.1)
    """)
    
    st.subheader("Critérios para Inaptidão Temporária")
    st.write("""
    - Lesões ou sintomas de enfermidades que possam comprometer a qualidade higiênico-sanitária dos alimentos
    - Afecções cutâneas, feridas e supurações
    - Sintomas e infecções respiratórias, gastrointestinais e oculares
    """)
    
    st.subheader("Condutas para Achados Específicos")
    st.write("""
    **1. Endolimax nana e Entamoeba coli:**
    - Normalmente não patológicos
    - Orientar acompanhamento médico assistencial
    - Não recomendar inaptidão nem tratamento
    
    **2. Amebíase ou giardíase:**
    - Prescrever SECNIDAZOL 1000mg (2 comprimidos em dose única)
    - Pode declarar aptidão com tratamento
    - Repetir exame após 14 dias
    
    **3. Outros achados:**
    - Analisar caso a caso
    - Pode manter ASO retido para solicitar exames ou relatórios
    - Discutir com medicina do trabalho da FORTNEER
    """)

elif menu == "Doenças Relacionadas ao Trabalho":
    st.header("Doenças Possivelmente Relacionadas ao Trabalho")
    
    st.write("""
    Em caso de suspeita, o médico deve proceder com investigação, após comunicação e discussão com o médico responsável pelo PCMSO.
    """)
    
    st.subheader("Critérios de Investigação (Resolução 2323/2022 - Art.2º)")
    st.write("""
    1. História clínica e ocupacional
    2. Estudo do local de trabalho
    3. Estudo da organização do trabalho
    4. Dados epidemiológicos
    5. Literatura científica
    6. Quadro clínico em trabalhadores com riscos semelhantes
    7. Identificação de riscos físicos, químicos, biológicos, etc.
    8. Depoimento dos trabalhadores
    9. Conhecimentos de outras disciplinas
    """)
    
    st.warning("""
    **Atenção:** É vedado determinar nexo causal sem observar estes critérios!
    """)
    
    st.subheader("Procedimentos em Caso de Confirmação")
    st.write("""
    1. Informar ao Médico Responsável pelo PCMSO (para emissão de CAT)
    2. Indicar afastamento quando necessário
    3. Encaminhar à Previdência para afastamentos >15 dias
    4. Realizar orientações previdenciárias e trabalhistas
    5. Sugerir melhorias no ambiente de trabalho
    6. Orientar o trabalhador sobre medidas de controle
    7. Colaborar com investigação do local de trabalho
    """)

elif menu == "Avaliações Não Ocupacionais":
    st.header("Avaliações e Consultas Não Ocupacionais")
    
    st.write("""
    A área de Saúde Ocupacional pode convocar trabalhadores para avaliações não relacionadas aos exames médicos ocupacionais.
    """)
    
    st.subheader("Situações")
    st.write("""
    - Atendimentos médicos ou de enfermagem não demandam ASO
    - Solicitações das lideranças para esclarecimento da condição de saúde
    - Orientações aos trabalhadores
    """)
    
    st.info("""
    **Observação:** Sempre respeitar o sigilo médico e legal.
    """)

elif menu == "Avaliação de PCD":
    st.header("Avaliações de PCD (Pessoas com Deficiência)")
    
    st.write("""
    Para fins de cumprimento do Art. 93 da Lei 8213/1991 (cotas).
    """)
    
    st.subheader("Base Legal")
    st.write("""
    - Convenção sobre os Direitos das Pessoas com Deficiência
    - Lei Brasileira de Inclusão (Lei 13.146/2015)
    - Lei 12.764/2012 (autismo)
    - Decretos 3298/1999, 5296/2004 e 6949/2009
    - Parecer CONJUR 444/2011
    - IN SIT/MTE 98/2012
    """)
    
    # Formulário para preenchimento do laudo
    with st.form("form_laudo_pcd"):
        st.subheader("Dados da Empresa")
        empresa_razao_social = st.text_input("Razão Social da Empresa")
        empresa_endereco = st.text_input("Endereço da Empresa")
        empresa_telefone = st.text_input("Telefone da Empresa")
        
        st.subheader("Dados do Trabalhador")
        nome = st.text_input("Nome Completo")
        matricula = st.text_input("Matrícula")
        data_nascimento = st.date_input("Data de Nascimento")
        rg = st.text_input("RG")
        sexo = st.radio("Sexo", ["Feminino", "Masculino"])
        
        st.subheader("Avaliação Médica")
        origem_deficiencia = st.selectbox("Origem da Deficiência", [
            "Acidente - Trabalho",
            "Acidente - Comum",
            "Adquirida",
            "Congênita",
            "Doença",
            "Hereditária",
            "Pós Operatório"
        ])
        cid = st.text_input("CID-10")
        data_manifestacao = st.date_input("Data de início das manifestações")
        pcd_reabilitado = st.radio("PCD Reabilitado", ["Sim", "Não"])
        
        st.subheader("Descrição da Deficiência")
        alteracoes = st.text_area("Descrição detalhada das alterações físicas, sensoriais, intelectuais e mentais")
        limitacoes = st.text_area("Descrição das limitações funcionais para atividades da vida diária e social")
        
        st.subheader("Tipo de Deficiência")
        deficiencia_fisica = st.checkbox("Deficiência Física")
        deficiencia_auditiva = st.checkbox("Deficiência Auditiva")
        deficiencia_visual = st.checkbox("Deficiência Visual")
        deficiencia_intelectual = st.checkbox("Deficiência Intelectual")
        deficiencia_mental = st.checkbox("Deficiência Mental")
        deficiencia_multipla = st.checkbox("Deficiência Múltipla")
        
        submitted = st.form_submit_button("Gerar Laudo PCD")
        
        if submitted:
            # Criar um novo PDF com os dados preenchidos
            buffer = BytesIO()
            c = canvas.Canvas(buffer)
            
            # Página 1
            c.setFont("Helvetica-Bold", 14)
            c.drawString(100, 800, "FORTNEER ENGENHARIA EIRELI")
            c.drawString(100, 785, empresa_endereco)
            c.drawString(100, 770, f"Fone: {empresa_telefone}")
            
            c.setFont("Helvetica-Bold", 16)
            c.drawString(100, 740, "LAUDO CARACTERIZADOR DE DEFICIÊNCIA")
            
            c.setFont("Helvetica", 10)
            c.drawString(100, 720, "De acordo com o Decreto 3.298/1999 e com a Instrução Normativa SIT/ MTE n.º 98 de 15/08/2012,")
            c.drawString(100, 705, "observados os dispositivos da Convenção sobre os Direitos das Pessoas com deficiência e Lei 12764/12")
            
            # Tabela de identificação
            c.setFont("Helvetica-Bold", 10)
            c.drawString(100, 680, "Identificação Empresa/Razão Social")
            c.drawString(350, 680, empresa_razao_social)
            
            c.drawString(100, 660, "Nome")
            c.drawString(350, 660, nome)
            
            c.drawString(100, 640, "Matrícula")
            c.drawString(350, 640, matricula)
            
            c.drawString(100, 620, "Data Nascimento")
            c.drawString(350, 620, str(data_nascimento))
            
            c.drawString(100, 600, "Documento RG:")
            c.drawString(350, 600, rg)
            
            c.drawString(100, 580, f"Sexo ({'X' if sexo == 'Feminino' else ' '})Feminino ({'X' if sexo == 'Masculino' else ' '})Masculino")
            
            # Avaliação
            c.drawString(100, 550, f"Origem Deficiência ({'X'}) {origem_deficiencia}")
            c.drawString(100, 530, f"CID {cid} Início das manifestações {data_manifestacao}")
            c.drawString(100, 510, f"PCD Reabilitado ({'X' if pcd_reabilitado == 'Sim' else ' '}) Sim ({'X' if pcd_reabilitado == 'Não' else ' '}) Não")
            
            # Descrições
            c.drawString(100, 480, "Descrição detalhada das alterações físicas, sensoriais, intelectuais e mentais:")
            textobject = c.beginText(100, 460)
            for line in alteracoes.split('\n'):
                textobject.textLine(line)
            c.drawText(textobject)
            
            c.drawString(100, 400, "Descrição das limitações funcionais para atividades da vida diária e social:")
            textobject = c.beginText(100, 380)
            for line in limitacoes.split('\n'):
                textobject.textLine(line)
            c.drawText(textobject)
            
            # Tipos de deficiência
            c.drawString(100, 320, "I - Deficiência Física")
            c.drawString(120, 300, f"({'X' if deficiencia_fisica else ' '}) Alteração Física - [descrição]")
            
            c.drawString(100, 270, "II - Deficiência Auditiva")
            c.drawString(120, 250, f"({'X' if deficiencia_auditiva else ' '}) Perda Auditiva - [descrição]")
            
            # [...] Continuar com os outros tipos de deficiência
            
            c.showPage()  # Página 2
            
            # Termo de ciência
            c.setFont("Helvetica-Bold", 14)
            c.drawString(100, 800, "FORTNEER ENGENHARIA EIRELI")
            c.drawString(100, 785, empresa_endereco)
            c.drawString(100, 770, f"Fone: {empresa_telefone}")
            
            c.setFont("Helvetica", 12)
            c.drawString(100, 730, "Estou ciente de que estou sendo enquadrado na cota de pessoas com deficiência/reabilitados da empresa.")
            c.drawString(100, 710, "Autorizo a apresentação deste Laudo e exames ao Ministério do Trabalho e Emprego.")
            
            c.drawString(100, 670, "Assinatura do Avaliado: ___________________________")
            c.drawString(100, 650, "Data: ____/____/____")
            
            c.save()
            
            pdf_bytes = buffer.getvalue()
            buffer.close()
            
            st.success("Laudo gerado com sucesso!")
            
            st.download_button(
                label="Baixar Laudo PCD",
                data=pdf_bytes,
                file_name=f"laudo_pcd_{nome.replace(' ', '_')}.pdf",
                mime="application/pdf"
            )

# Rodapé
st.markdown("---")
st.write(""" 
**FORTNEER - ASSESSORIA PARA REGULARIZAÇÃO EMPRESARIAL**

Atualizado em: 29 DE MAIO DE 2025  
""")
