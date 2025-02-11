import streamlit as st
from llm_search import get_link
from link_structured import structured_link
from image_extract import get_image
from llm_for_json_format import json_format
from website_link_extract import get_link_from_website
from serpapi_search import google_search


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
                # structured_url = google_search(data)
                if structured_url['found']:
                    working_photos = get_image(structured_url)
                    web_other_links = get_link_from_website(structured_url)
                    result = json_format(
                        data=data,
                        working_photos=working_photos,
                        url=structured_url,
                        other_links = web_other_links
                    )

                    st.success("Processing Complete!")
                    st.write(structured_url)
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




    #                     [
    #     {
    #         \"id\": 8608,
    #         \"name\": \"Xelent Solution\",
    #         \"address\": \"p 58 Usman town\",
    #         \"city\": \"Faisalabad\",
    #         \"province\": \"Punjab\",
    #         \"post_code\": \"38000\",
    #         \"phone\": \"+92 300 1076788\",
    #         \"contact_name\": null,
    #         \"title\": null,
    #         \"employee_count\": \"1 TO 20\",
    #         \"employee_code\": \"1\",
    #         \"annual_sales\": \"LESS THAN $500,000\",
    #         \"sale_code\": \"1\",
    #         \"sic_code\": null,
    #         \"industry\": \"Software House\",
    #         \"type\": \"apparel\",
    #         \"country\": \"pakistan\",
    #     }
    # ]