import time
import os
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.mention import mention
from streamlit_extras.streaming_write import write
from pages.main_page.main_page import main_page
from pages.instruction_page.instruction_page import instruction_page
# from models.openai.OpenaiLM import OpenaiLM
# from models.spark.spark_utils import *


# from PIL import Image
# image = Image.open('./res/img/cs.png')



if __name__ == '__main__':

    st.set_page_config(
        page_title='主页',
        page_icon='./res/img/logo.ico',
        layout='wide',
        # menu_items={
        #     'About': f"""欢迎使用 {PAGE_TITLE}"""
        # }
    )


    pages = {
        "主页": {
            "icon": "hdd-stack",
            "func": main_page,
        },
        # "使用指南": {
        #     "icon": "hdd-stack",
        #     "func": instruction_page,
        # },
    }

    # Using "with" notation
    with st.sidebar:
        st.image(
            os.path.join(
                "res/img",
                "logo_new.png"
            ),
            use_column_width=True
        )

        options = list(pages)
        icons = [x["icon"] for x in pages.values()]

        st.divider()

        default_index = 0
        selected_page = option_menu(
            "",
            options=options,
            icons=icons,
            # menu_icon="chat-quote",
            default_index=default_index,
        )

    if selected_page in pages:
        pages[selected_page]["func"]()

