import os

from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from app.ports.resumidor_port import ResumidorPort
from app.utilities.google_services import get_secrets_values

os.load_dotenv()

DEBUG = os.getenv("DEBUG", True)

class GeminiFlashAdapter(ResumidorPort):
    """
    Adapter that implements ResumidorPort using Google's Gemini Flash 2.5 model.
    """

    def __init__(self):
        self.api_key = get_secrets_values("secrets_ai_summarizer", debug=DEBUG)["google_api_key"]

    def resumir(self, texto: str) -> str:
        """
        Summarizes the provided text using the Gemini Flash model.
        args:
            texto (str): The text to be summarized.
        returns:
            str: The summarized text.
        """
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash", google_api_key=self.api_key, temperature=0.3
        )

        prompt = PromptTemplate(
            input_variables=["texto"],
            template="Por favor, resume el siguiente texto de forma clara y concisa:\n\n{texto}",
        )

        chain = prompt | llm
        resumen = chain.invoke({"texto": texto})
        return resumen.content


if __name__ == "__main__":
    adaptador = GeminiFlashAdapter()
    texto = "El cerdito del medio, que era medio perezoso, medio prestó atención a las palabras de mamá cerdita y construyó una casita de palos. La casita le quedó chueca porque como era medio perezoso no quiso leer las instrucciones para construirla."
    resumen = adaptador.resumir(texto)
    print(resumen)
