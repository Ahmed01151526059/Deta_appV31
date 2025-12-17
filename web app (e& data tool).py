import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- Configuration for Styling ---
BRAND_RED = "#E60000"

# =========================================================================
# === STATE MANAGEMENT (GUI Only) ===
# =========================================================================

# Initialize session state for navigation
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.selected_source = "Tableau"
    
    # Mock data for showing the grid and combos
    st.session_state.current_df = pd.DataFrame(
        np.random.randint(0, 100, size=(10, 4)),
        columns=['Metric_A', 'Dimension_B', 'Date_C', 'Value_D']
    )
    st.session_state.workbooks = [{"id": "wb1", "name": "Sales Summary (Mock)"}]

# =========================================================================
# === UI LAYOUT FUNCTIONS ===
# =========================================================================

def login_screen():
    st.title(f"e& Data Tool :red[Web UI (Login)]")
    st.subheader("Select Data Source")
    
    col1, col2 = st.columns(2)
    
    with col1:
        source = st.selectbox(
            "Source Type",
            options=["Tableau", "CSV/Excel", "Power BI", "Database"],
        )

    with col2:
        st.subheader("Connection Details")
        st.text_input("Username")
        st.text_input("Password", type="password")
        
        if st.button("Connect", type="primary"):
            # Mock login success to show the main screens
            st.session_state.logged_in = True
            st.session_state.selected_source = source
            st.rerun()

def build_home_view():
    st.subheader("📊 Data & Chat (Tkinter: Home Tab)")

    # --- Top Control Bar (Tkinter: top frame content) ---
    col1, col2, col3 = st.columns([3, 3, 2])
    
    with col1:
        st.selectbox("Select Source:", ["Sales Summary (Mock)"])
    
    with col2:
        st.selectbox("Select View/Table:", ["Main Table"])
    
    with col3:
        st.markdown("<div style='height:25px;'></div>", unsafe_allow_html=True)
        st.button("DISPLAY DATA", type="primary")

    # --- Data Grid Display (Tkinter: tree) ---
    st.markdown("---")
    st.subheader("Data Grid Preview (Tkinter: tree)")
    st.dataframe(st.session_state.current_df.head(10), use_container_width=True)
    
    # --- AI Chat Section (Tkinter: chat_hist, chat_entry) ---
    st.markdown("---")
    st.subheader("AI Assistant")
    
    # Input Row
    col_mode, col_input, col_btn = st.columns([2, 6, 1])
    
    with col_mode:
        st.selectbox("Mode", ["Answering", "Generative", "SQL Query"], label_visibility="collapsed")
    
    with col_input:
        st.text_input("Enter your question...", label_visibility="collapsed")
        
    with col_btn:
        st.button("➤", type="primary", use_container_width=True)
        
    st.text_area("Chat History / Suggestions", height=150, disabled=True, 
                 value="AI: Conversation history appears here, with result buttons.")


def build_manual_view():
    st.subheader("🛠 Manual Builder (Tkinter: Manual Tab)")

    # --- Chart Configuration (Tkinter: controls frame) ---
    with st.expander("Chart Configuration", expanded=True):
        col_x, col_y, col_agg, col_kind = st.columns(4)

        with col_kind:
            st.selectbox("Chart Type", ["bar", "line", "card"], key='man_kind')

        with col_x:
            st.selectbox("X-Axis (Group By)", st.session_state.current_df.columns.tolist(), key='man_x_ui')

        with col_y:
            st.selectbox("Y-Axis (Measure)", st.session_state.current_df.columns.tolist(), key='man_y_ui')
            
        with col_agg:
            st.selectbox("Aggregation", ["Sum", "Avg", "Count"], key='man_agg_ui')
        
        st.button("Add Chart to Dashboard", type="primary")

    # --- Filter Section (Tkinter: filter_frame) ---
    st.markdown("---")
    st.subheader("Page Filter (Tkinter: filter_frame)")
    col_f1, col_f2, col_f3, col_f4 = st.columns(4)
    with col_f1:
        st.selectbox("Column", st.session_state.current_df.columns.tolist())
    with col_f2:
        st.selectbox("Hierarchy", ["Exact", "Year", "Month"])
    with col_f3:
        st.text_input("Value")
    with col_f4:
        st.markdown("<div style='height:25px;'></div>", unsafe_allow_html=True)
        st.button("Apply Filter", type="success")
        st.button("Reset Filter", type="warning")
        
    # --- Dashboard Area (Tkinter: manual_canvas) ---
    st.markdown("---")
    st.subheader("Interactive Dashboard Grid (Tkinter: manual_canvas)")
    
    # Mock chart rendering placeholder
    cols = st.columns(2)
    for i in range(2):
        with cols[i]:
            st.markdown(f"**Mock Chart {i+1}**")
            with st.container(border=True):
                 fig, ax = plt.subplots(figsize=(6, 4))
                 ax.set_title(f"Chart Placeholder {i+1}")
                 ax.plot([0, 1], [0, 1], color=BRAND_RED)
                 st.pyplot(fig, use_container_width=True)
                 plt.close(fig) 
                 
                 st.button("Remove Chart", key=f"remove_mock_{i}")


def build_ml_view():
    st.subheader("📈 Advanced Analytics (Tkinter: ML Tab)")
    
    st.info("This section replicates the layout for model configuration and results.")

    # --- Configuration ---
    st.markdown("### 1. Model Setup (Tkinter: ml_config_frame)")
    col_target, col_task, col_algo = st.columns(3)

    with col_target:
        st.selectbox("Target (Y) Column:", st.session_state.current_df.columns.tolist(), key='ml_target')
    
    with col_task:
        st.selectbox("Task Type:", ["Regression", "Classification"])
        
    with col_algo:
        st.selectbox("Algorithm:", ["Linear Regression", "Random Forest"])

    # --- Features and Actions ---
    st.markdown("### 2. Features and Actions")
    st.multiselect("Select Features:", st.session_state.current_df.columns.tolist())
    st.button("🚀 Train Model", type="primary")

    # --- Results (Tkinter: ml_viz_frame) ---
    st.markdown("### 3. Results")
    st.text_area("Metrics Output", height=100, disabled=True, value="Metrics will appear here (R2, RMSE, Accuracy)")
    st.info("Plot area placeholder for Actual vs Predicted.")


# =========================================================================
# === MAIN APPLICATION FLOW ===
# =========================================================================

def main_app():
    # Set the wide layout for better space utilization (like maximizing a desktop app)
    st.set_page_config(layout="wide")
    st.title(f"e& AI Data Tool :red[Web UI Test]")

    # --- Sidebar Navigation (Replaces Tkinter Sidebar) ---
    with st.sidebar:
        st.header("Navigation")
        
        if st.session_state.logged_in:
            selected_tab = st.radio(
                "Select View",
                options=["Data & Chat", "Manual Builder", "Advanced Analytics"],
                index=0,
                key='web_tabs'
            )
            
            st.markdown("---")
            if st.button("Logout"):
                st.session_state.logged_in = False
                st.rerun()
        else:
             st.info("Please log in first.")
             selected_tab = None

        st.markdown("---")
        st.button("📄 Export to PDF")
             
    # --- Main Content Area ---
    if not st.session_state.logged_in:
        login_screen()
    else:
        # Tab Content Rendering
        if selected_tab == "Data & Chat":
            build_home_view()
        elif selected_tab == "Manual Builder":
            build_manual_view()
        elif selected_tab == "Advanced Analytics":
            build_ml_view()

if __name__ == '__main__':
    main_app()
