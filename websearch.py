import streamlit as st
from ddg import Duckduckgo

ddg_client = Duckduckgo()

def web_search(query: str = "", limit: int = 10) -> list:
    results = ddg_client.search(f"Nachrichten über '{query}'")
    st.warning(results["data"])
    if results:
        return results["data"][:limit]
    else:
        return []


st.title("Web Search")

query = st.text_input("Enter a query")
limit = st.slider("Number of results", 1, 20, 10)

if st.button("Search"):
    results = web_search(query, limit)
    if results:
        for result in results:
            st.write(result["title"])
            st.write(result["url"])
            st.write(result["description"])
            st.write("---")
    else:
        st.write("No results found")

