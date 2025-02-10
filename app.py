import streamlit as st
from llm_search import get_link
from link_structured import structured_link
from image_extract import get_image
from llm_for_json_format import json_format


st.set_page_config(page_title="Website Search", page_icon="🖥️")


st.title("🔍 Search for website with JSON data")


data = st.text_area("Enter your business data (JSON format):", height=200)


if st.button("Process Data"):
    if not data:
        st.warning("Please enter some data to process!")
    else:
        with st.spinner("Processing your data..."):
            try:
                raw_url = get_link(data)
                structured_url = structured_link(raw_url)
                
                if structured_url['found']:
                    working_photos = get_image(structured_url)
                    result = json_format(
                        data=data,
                        working_photos=working_photos,
                        url=structured_url
                    )

                    st.success("Processing Complete!")
                    st.subheader("Formatted Output:")
                    st.json(result)

                    st.download_button(
                        label="Download JSON",
                        data=str(result),
                        file_name="business_data.json",
                        mime="application/json"
                    )
                else:
                    st.error("Error: No valid website link found")
                    
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")