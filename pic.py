import streamlit as st
from datetime import datetime
from reportlab.pdfgen import canvas
from io import BytesIO
import base64

# Configurações da página
st.set_page_config(
    page_title="PIC - FORTNEER",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados
def local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except:
        # CSS padrão se o arquivo não existir
        st.markdown("""
        <style>
            .header-subtitle {
                font-size: 1.1rem;
                color: #555;
                margin-top: -10px;
            }
            .header-location {
                font-style: italic;
                color: #777;
            }
            .sidebar-header {
                margin-bottom: 20px;
            }
            .quick-info {
                background-color: #f8f9fa;
                padding: 15px;
                border-radius: 10px;
                margin-top: 20px;
            }
            .status-box {
                padding: 15px;
                border-radius: 8px;
                margin-bottom: 15px;
                border-left: 5px solid;
            }
            .status-box.green {
                background-color: #e6f7e6;
                border-color: #28a745;
            }
            .status-box.yellow {
                background-color: #fff8e6;
                border-color: #ffc107;
            }
            .status-box.red {
                background-color: #ffebee;
                border-color: #dc3545;
            }
            .status-dot {
                height: 15px;
                width: 15px;
                border-radius: 50%;
                display: inline-block;
                margin-right: 10px;
            }
            .green .status-dot { background-color: #28a745; }
            .yellow .status-dot { background-color: #ffc107; }
            .red .status-dot { background-color: #dc3545; }
            .status-text {
                display: inline-block;
                vertical-align: top;
                width: calc(100% - 30px);
            }
            .grid-container {
                display: grid;
                grid-template-columns: repeat(2, 1fr);
                gap: 10px;
                margin: 15px 0;
            }
            .grid-item {
                background-color: #f8f9fa;
                padding: 10px;
                border-radius: 5px;
                border-left: 3px solid #6c757d;
            }
            .info-box {
                background-color: #e7f5ff;
                padding: 15px;
                border-radius: 8px;
                margin: 15px 0;
                border-left: 5px solid #1c7ed6;
            }
            .footer {
                margin-top: 50px;
                padding: 20px 0;
                text-align: center;
                color: #666;
                font-size: 0.9rem;
            }
        </style>
        """, unsafe_allow_html=True)

local_css("styles.css")

# Cabeçalho moderno
def render_header():
    col1, col2 = st.columns([1, 4])
    with col1:
        # Placeholder para logo (removida a dependência de arquivo)
        st.markdown("""
        <div style="width:120px; height:120px; background:#eee; display:flex; 
                    align-items:center; justify-content:center; border-radius:10px;">
            LOGO
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.title("Protocolo de Interpretação e Conduta Médica")
        st.markdown("""
        <div class="header-subtitle">
            FORTNEER - Assessoria para Regularização Empresarial<br>
            <span class="header-location">Sombrio & Morro da Fumaça</span>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")

# Menu lateral moderno
def render_sidebar():
    with st.sidebar:
        # Placeholder para logo médico (removida a dependência de arquivo)
        st.markdown("""
        <div style="width:120px; height:120px; background:#eee; display:flex; 
                    align-items:center; justify-content:center; border-radius:10px; margin:0 auto;">
            LOGO
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="sidebar-header">
            <h3>Menu de Navegação</h3>
        </div>
        """, unsafe_allow_html=True)
        
        menu_options = {
            "Introdução": "📋",
            "Aptidão para Atividades Críticas": "⚠️",
            "Exames com Normas Específicas": "🔍",
            "Afastamento e Restrições": "🚧",
            "Retorno ao Trabalho": "↩️",
            "Manipuladores de Alimentos": "🍽️",
            "Doenças Relacionadas ao Trabalho": "🏭",
            "Avaliações Não Ocupacionais": "🩺",
            "Avaliação de PCD": "♿"
        }
        
        selected = st.radio(
            "Selecione a seção:",
            options=list(menu_options.keys()),
            format_func=lambda x: f"{menu_options[x]} {x}",
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        
        # Seção de informações rápidas
        st.markdown("""
        <div class="quick-info">
            <h4>📅 Atualização</h4>
            <p>Versão: 2.1.0 (Maio/2025)</p>
            
            <h4>📞 Contato</h4>
            <p>suporte@fortneer.com.br</p>
            <p>(48) 99999-9999</p>
        </div>
        """, unsafe_allow_html=True)
        
    return selected

# Componente de status (verde/amarelo/vermelho)
def status_indicator(status, text):
    if status == "green":
        st.markdown(f"""
        <div class="status-box green">
            <div class="status-dot"></div>
            <div class="status-text"><strong>Sinal Verde</strong><br>{text}</div>
        </div>
        """, unsafe_allow_html=True)
    elif status == "yellow":
        st.markdown(f"""
        <div class="status-box yellow">
            <div class="status-dot"></div>
            <div class="status-text"><strong>Sinal Amarelo</strong><br>{text}</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="status-box red">
            <div class="status-dot"></div>
            <div class="status-text"><strong>Sinal Vermelho</strong><br>{text}</div>
        </div>
        """, unsafe_allow_html=True)

# Página de introdução
def render_intro():
    st.header("📋 Introdução")
    
    with st.expander("📌 Visão Geral", expanded=True):
        st.write("""
        A conduta médica para interpretação dos exames e definição de aptidão ao trabalho deve seguir critérios técnico-científicos, 
        éticos e normativos. Este protocolo foi elaborado baseado nos preceitos éticos e na legislação vigente e tem por abrangência 
        todos os atendimentos realizados por médicos em agendamentos feitos pela FORTNEER ou por suas empresas clientes.
        """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.expander("🧭 Princípios Gerais", expanded=True):
            st.markdown("""
            1. **Alinhamento normativo:** Seguir os critérios deste protocolo, conforme NR-7 e Resolução 2323/2022 do CFM.
            2. **Flexibilidade condicionada:** Condutas diferentes são permitidas quando justificadas e registradas.
            3. **Suporte técnico:** Em caso de dúvidas, contatar o responsável pela saúde ocupacional da FORTNEER.
            4. **Transparência:** Trabalhadores devem ser informados sobre exames e resultados.
            5. **Conformidade legal:** Observar toda a Resolução 2323/2022 do CFM.
            """)
    
    with col2:
        with st.expander("⚖️ Responsabilidades", expanded=True):
            st.markdown("""
            - **Solicitação de exames:** O médico pode solicitar repetição ou novos exames para formação de convicção técnica.
            - **Registro documental:** Todas as condutas devem ser justificadas tecnicamente e discutidas com o médico responsável pelo PCMSO.
            - **Sigilo e ética:** Manter confidencialidade dos dados médicos conforme legislação.
            """)
    
    st.markdown("---")
    
    with st.expander("📚 Documentação de Referência", expanded=False):
        st.markdown("""
        - **NR-7:** Programa de Controle Médico de Saúde Ocupacional
        - **Resolução CFM 2323/2022:** Diretrizes para saúde ocupacional
        - **CLT:** Consolidação das Leis do Trabalho
        - **Lei 605/1949:** Dispõe sobre o repouso semanal remunerado
        """)

# Página de aptidão para atividades críticas
def render_critical_activities():
    st.header("⚠️ Aptidão para Atividades Críticas")
    
    with st.expander("ℹ️ Definição", expanded=True):
        st.write("""
        Atividades críticas são definidas na NR-7 como aquelas que exigem avaliação médica específica para definir a aptidão do empregado.
        Estas atividades envolvem riscos significativos que podem ser agravados por condições de saúde do trabalhador.
        """)
    
    tab1, tab2, tab3 = st.tabs(["📋 Exemplos", "🚦 Critério Tricolor", "🔍 Avaliações"])
    
    with tab1:
        st.subheader("Exemplos de Atividades Críticas")
        st.markdown("""
        <div class="grid-container">
            <div class="grid-item">📌 Trabalhos com risco de queda</div>
            <div class="grid-item">📌 Espaços confinados</div>
            <div class="grid-item">📌 Operação de máquinas perigosas</div>
            <div class="grid-item">📌 Condução de veículos</div>
            <div class="grid-item">📌 Risco de choques elétricos</div>
            <div class="grid-item">📌 Pontes rolantes</div>
        </div>
        """, unsafe_allow_html=True)
    
    with tab2:
        st.subheader("Sistema de Classificação")
        
        cols = st.columns(3)
        with cols[0]:
            status_indicator("green", "Condição que não deve ser considerada como critério de incompatibilidade.")
        with cols[1]:
            status_indicator("yellow", "Condição que merece investigação e/ou acompanhamento. Avaliar caso a caso.")
        with cols[2]:
            status_indicator("red", "Existe contraindicação para a execução de atividades críticas.")
        
        st.markdown("""
        <div class="info-box">
            💡 Este sistema visa padronizar a avaliação médica, mas não substitui o julgamento clínico do profissional.
        </div>
        """, unsafe_allow_html=True)
    
    with tab3:
        st.subheader("Avaliações Específicas")
        
        evaluation = st.selectbox("Selecione o tipo de avaliação:", [
            "Acuidade Visual e Avaliação Oftalmológica",
            "Arritmias Cardíacas e ECG",
            "Hipertensão Arterial",
            "Diabetes e Glicemia em Jejum",
            "Obesidade",
            "Anemias e Hemograma",
            "Equilíbrio e Consciência",
            "Fatores Psicossociais",
            "Acuidade Auditiva"
        ], key="eval_select")
        
        if evaluation == "Acuidade Visual e Avaliação Oftalmológica":
            st.subheader("👁️ Acuidade Visual")
            
            cols = st.columns(3)
            with cols[0]:
                status_indicator("green", """
                - AV ≥ 20/40 em cada olho
                - AV ≥ 20/30 + PL em um olho
                - Visão periférica ≥ 60° cada olho
                """)
            with cols[1]:
                status_indicator("yellow", """
                - Visão monocular com perda antiga
                - Visão periférica ≥ 120° em um olho
                """)
            with cols[2]:
                status_indicator("red", """
                - Visão monocular recente
                - Perda visual significativa
                """)
            
            st.markdown("---")
            st.write("""
            **Critérios adicionais:**
            - Teste de visão de cores para atividades que exigem discriminação cromática
            - Avaliação de campo visual para motoristas profissionais
            """)
        
        elif evaluation == "Arritmias Cardíacas e ECG":
            st.subheader("❤️ Arritmias Cardíacas e ECG")
            
            cols = st.columns(3)
            with cols[0]:
                status_indicator("green", """
                - Alterações de repolarização
                - Extrassístoles atriais isoladas
                - BAV 1° grau
                - BRD isolado
                """)
            with cols[1]:
                status_indicator("yellow", """
                - Sobrecarga de VE
                - Extrassístoles frequentes
                - BAV 2° grau tipo I
                - BRE (avaliar)
                """)
            with cols[2]:
                status_indicator("red", """
                - BAV 2° grau tipo II
                - BAV total
                - Taquicardia SV Paroxística
                """)
            
            st.markdown("---")
            st.write("""
            **Recomendações:**
            - Encaminhar para avaliação cardiológica em casos amarelos/vermelhos
            - Considerar Holter 24h quando necessário
            """)

# Página de avaliação de PCD
def render_pcd_assessment():
    st.header("♿ Avaliação de PCD")
    
    with st.expander("📌 Base Legal", expanded=False):
        st.markdown("""
        - **Convenção sobre os Direitos das Pessoas com Deficiência**
        - **Lei Brasileira de Inclusão (Lei 13.146/2015)**
        - **Lei 12.764/2012** (autismo)
        - **Decretos 3298/1999, 5296/2004 e 6949/2009**
        - **Parecer CONJUR 444/2011**
        - **IN SIT/MTE 98/2012**
        """)
    
    with st.form("form_laudo_pcd", clear_on_submit=False):
        st.subheader("📝 Dados para Laudo PCD")
        
        tabs = st.tabs(["Dados Empresa", "Dados Trabalhador", "Avaliação Médica", "Revisão"])
        
        with tabs[0]:
            st.text_input("Razão Social da Empresa*", key="empresa_razao")
            st.text_input("Endereço Completo*", key="empresa_endereco")
            st.text_input("Telefone para Contato*", key="empresa_telefone")
        
        with tabs[1]:
            cols = st.columns(2)
            with cols[0]:
                st.text_input("Nome Completo*", key="nome")
                st.date_input("Data de Nascimento*", key="data_nascimento")
            with cols[1]:
                st.text_input("Matrícula (se aplicável)", key="matricula")
                st.text_input("RG*", key="rg")
            
            st.radio("Sexo*", ["Feminino", "Masculino", "Outro"], key="sexo", horizontal=True)
        
        with tabs[2]:
            cols = st.columns(2)
            with cols[0]:
                st.selectbox("Origem da Deficiência*", [
                    "Acidente - Trabalho",
                    "Acidente - Comum",
                    "Adquirida",
                    "Congênita",
                    "Doença",
                    "Hereditária",
                    "Pós Operatório"
                ], key="origem_deficiencia")
                
                st.text_input("CID-10*", key="cid")
            with cols[1]:
                st.date_input("Data de início das manifestações*", key="data_manifestacao")
                st.radio("PCD Reabilitado*", ["Sim", "Não"], key="pcd_reabilitado", horizontal=True)
            
            st.text_area("Descrição detalhada das alterações*", key="alteracoes", height=100)
            st.text_area("Limitações funcionais para atividades diárias*", key="limitacoes", height=100)
            
            st.subheader("Tipo de Deficiência*")
            cols = st.columns(3)
            with cols[0]:
                st.checkbox("Deficiência Física", key="deficiencia_fisica")
                st.checkbox("Deficiência Auditiva", key="deficiencia_auditiva")
            with cols[1]:
                st.checkbox("Deficiência Visual", key="deficiencia_visual")
                st.checkbox("Deficiência Intelectual", key="deficiencia_intelectual")
            with cols[2]:
                st.checkbox("Deficiência Mental", key="deficiencia_mental")
                st.checkbox("Deficiência Múltipla", key="deficiencia_multipla")
        
        with tabs[3]:
            st.subheader("Resumo do Laudo")
            
            if st.session_state.get('nome'):
                cols = st.columns(2)
                with cols[0]:
                    st.markdown("**Dados do Trabalhador**")
                    st.write(f"Nome: {st.session_state.nome}")
                    st.write(f"Nascimento: {st.session_state.data_nascimento}")
                    st.write(f"RG: {st.session_state.rg}")
                
                with cols[1]:
                    st.markdown("**Avaliação Médica**")
                    st.write(f"Origem: {st.session_state.origem_deficiencia}")
                    st.write(f"CID-10: {st.session_state.cid}")
                    st.write(f"Reabilitado: {st.session_state.pcd_reabilitado}")
                
                st.markdown("**Descrição das Alterações**")
                st.write(st.session_state.alteracoes)
                
                st.markdown("**Tipos de Deficiência**")
                tipos = []
                if st.session_state.deficiencia_fisica: tipos.append("Física")
                if st.session_state.deficiencia_auditiva: tipos.append("Auditiva")
                if st.session_state.deficiencia_visual: tipos.append("Visual")
                if st.session_state.deficiencia_intelectual: tipos.append("Intelectual")
                if st.session_state.deficiencia_mental: tipos.append("Mental")
                if st.session_state.deficiencia_multipla: tipos.append("Múltipla")
                
                st.write(", ".join(tipos) if tipos else "Nenhum tipo selecionado")
            else:
                st.warning("Preencha os dados nas abas anteriores para visualizar o resumo.")
        
        submitted = st.form_submit_button("✅ Gerar Laudo PCD")
        
        if submitted:
            # Validação dos campos obrigatórios
            required_fields = [
                'empresa_razao', 'empresa_endereco', 'empresa_telefone',
                'nome', 'data_nascimento', 'rg', 'origem_deficiencia',
                'cid', 'data_manifestacao', 'alteracoes', 'limitacoes'
            ]
            
            missing_fields = [field for field in required_fields if not st.session_state.get(field)]
            
            if missing_fields:
                st.error(f"Por favor, preencha todos os campos obrigatórios. Campos faltantes: {', '.join(missing_fields)}")
            else:
                # Criar PDF (simplificado para exemplo)
                buffer = BytesIO()
                c = canvas.Canvas(buffer)
                
                # Cabeçalho
                c.setFont("Helvetica-Bold", 14)
                c.drawString(100, 800, "LAUDO MÉDICO - CARACTERIZAÇÃO DE PCD")
                c.drawString(100, 780, f"Emitido em: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
                
                # Dados da empresa
                c.setFont("Helvetica-Bold", 12)
                c.drawString(100, 750, "Dados da Empresa:")
                c.setFont("Helvetica", 12)
                c.drawString(100, 730, f"Razão Social: {st.session_state.empresa_razao}")
                c.drawString(100, 710, f"Endereço: {st.session_state.empresa_endereco}")
                c.drawString(100, 690, f"Telefone: {st.session_state.empresa_telefone}")
                
                # Dados do trabalhador
                c.setFont("Helvetica-Bold", 12)
                c.drawString(100, 660, "Dados do Trabalhador:")
                c.setFont("Helvetica", 12)
                c.drawString(100, 640, f"Nome: {st.session_state.nome}")
                c.drawString(100, 620, f"Data Nascimento: {st.session_state.data_nascimento}")
                c.drawString(100, 600, f"RG: {st.session_state.rg}")
                c.drawString(100, 580, f"Sexo: {st.session_state.sexo}")
                
                # Avaliação médica
                c.setFont("Helvetica-Bold", 12)
                c.drawString(100, 550, "Avaliação Médica:")
                c.setFont("Helvetica", 12)
                c.drawString(100, 530, f"Origem: {st.session_state.origem_deficiencia}")
                c.drawString(100, 510, f"CID-10: {st.session_state.cid}")
                c.drawString(100, 490, f"Reabilitado: {st.session_state.pcd_reabilitado}")
                
                # Descrições
                c.drawString(100, 460, "Descrição das Alterações:")
                textobject = c.beginText(100, 440)
                for line in st.session_state.alteracoes.split('\n'):
                    textobject.textLine(line)
                c.drawText(textobject)
                
                c.drawString(100, 380, "Limitações Funcionais:")
                textobject = c.beginText(100, 360)
                for line in st.session_state.limitacoes.split('\n'):
                    textobject.textLine(line)
                c.drawText(textobject)
                
                c.showPage()
                
                # Termo de ciência
                c.setFont("Helvetica-Bold", 14)
                c.drawString(100, 800, "TERMO DE CIÊNCIA")
                
                c.setFont("Helvetica", 12)
                c.drawString(100, 770, "Eu, ________________________________________________________,")
                c.drawString(100, 750, "RG ________________________________________________________,")
                c.drawString(100, 730, "declaro que estou ciente do conteúdo deste laudo e autorizo sua utilização")
                c.drawString(100, 710, "para os fins legais pertinentes, conforme legislação vigente.")
                
                c.drawString(100, 670, "Assinatura: _________________________________________________")
                c.drawString(100, 650, "Data: ____/____/____")
                
                c.save()
                
                pdf_bytes = buffer.getvalue()
                buffer.close()
                
                st.success("Laudo gerado com sucesso!")
                
                st.download_button(
                    label="⬇️ Baixar Laudo PCD",
                    data=pdf_bytes,
                    file_name=f"laudo_pcd_{st.session_state.nome.replace(' ', '_')}.pdf",
                    mime="application/pdf"
                )

# Rodapé profissional
def render_footer():
    st.markdown("---")
    st.markdown("""
    <div class="footer">
        <div class="footer-content">
            <div class="footer-info">
                <h4>FORTNEER - Assessoria para Regularização Empresarial</h4>
                <p>Sombrio & Morro da Fumaça - SC</p>
                <p>Atualizado em: {}</p>
            </div>
        </div>
    </div>
    """.format(datetime.now().strftime("%d/%m/%Y")), 
    unsafe_allow_html=True)

# Página principal
def main():
    render_header()
    selected_menu = render_sidebar()
    
    if selected_menu == "Introdução":
        render_intro()
    elif selected_menu == "Aptidão para Atividades Críticas":
        render_critical_activities()
    elif selected_menu == "Avaliação de PCD":
        render_pcd_assessment()
    # ... outras páginas
    
    render_footer()

if __name__ == "__main__":
    main()
