import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from app.ports.resumidor_port import ResumidorPort


class GeminiProAdapter(ResumidorPort):
    """
    Adapter that implements ResumidorPort using Google's Gemini Pro 2.5 model.
    """

    def __init__(self):
        load_dotenv()
        if "GOOGLE_API_KEY" not in os.environ:
            raise ValueError("GOOGLE_API_KEY is not set in environment variables.")
        self.api_key = os.environ["GOOGLE_API_KEY"]

    def resumir(self, texto: str) -> str:
        """
        Summarizes the provided text using the Gemini Pro model.
        args:
            texto (str): The text to be summarized.
        returns:
            str: The summarized text.
        """
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-pro", google_api_key=self.api_key, temperature=0.3
        )

        prompt = PromptTemplate(
            input_variables=["texto"],
            template="Responde con el resumen del siguiente texto: \n\n{texto}, no añadas nada más.",
        )

        chain = prompt | llm
        resumen = chain.invoke({"texto": texto})
        return resumen.content


if __name__ == "__main__":
    adaptador = GeminiProAdapter()
    texto = "El cerdito del medio, que era medio perezoso, medio prestó atención a las palabras de mamá cerdita y construyó una casita de palos. La casita le quedó chueca porque como era medio perezoso no quiso leer las instrucciones para construirla."
    resumen = adaptador.resumir(texto)
    print(resumen)
