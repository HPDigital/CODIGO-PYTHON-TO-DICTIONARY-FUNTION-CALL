"""
CODIGO PYTHON TO DICTIONARY FUNTION CALL
"""

#!/usr/bin/env python
# coding: utf-8

# In[2]:


import ast
import json

def extract_function_details(code):
    # Analiza el código fuente para obtener el árbol de sintaxis abstracta (AST)
    tree = ast.parse(code)

    functions = []

    # Recorre el árbol de sintaxis para encontrar todas las definiciones de funciones
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            function_details = {
                "type": "function",
                "function": {
                    "name": node.name,
                    "description": "Description not provided.",  # Debería ser proporcionada manualmente o extraída de comentarios
                    "parameters": {
                        "type": "object",
                        "properties": {},
                        "required": []
                    }
                }
            }

            # Extrae detalles de los parámetros
            for arg in node.args.args:
                param_name = arg.arg
                function_details["function"]["parameters"]["properties"][param_name] = {
                    "type": "string",  # Asumimos string por defecto, debería ajustarse según el uso
                    "description": "No description provided."  # Debería ser proporcionada manualmente o extraída de comentarios
                }
                function_details["function"]["parameters"]["required"].append(param_name)

            functions.append(function_details)

    return json.dumps(functions, indent=4)

# Ejemplo de uso
# code = """
# def get_order_details(order_id):
#     url = "http://your_api_endpoint/order_info"
#     params = {'order_id': order_id}
#     response = requests.post(url, params=params)
#     if response.status_code == 200:
#         return response.json()['Result'][0]
#     else:
#         return f"Error: Unable to fetch order details. Status code: {response.status_code}"
# """

code = """
def read_and_chunk_file(file_path, chunk_size=4500):
    # Leer el documento completo
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Dividir el documento en chunks
    chunks = textwrap.wrap(content, chunk_size, break_long_words=False, replace_whitespace=False)
    return chunks
"""




# Extrae detalles de la función y los imprime en formato JSON
print(extract_function_details(code))


# In[ ]:






if __name__ == "__main__":
    pass
