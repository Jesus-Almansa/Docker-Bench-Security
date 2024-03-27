import json

def json2html(input_file, output_file):

    # Aquí va tu código para leer y analizar el JSON desde un archivo o una cadena.

    with open(input_file, 'r') as f:
        data = json.load(f)

    # Generar HTML
    html = "<!DOCTYPE html>\n<html>\n<head>\n<title>Docker Bench Security Report</title>\n</head>\n<body>\n"

    # Agregar información general
    html += "<h1>Docker Bench Security Report</h1>\n"
    html += f"<p>Version: {data['dockerbenchsecurity']}</p>\n"
    html += f"<p>Start Time: {data['start']}</p>\n"
    html += f"<p>End Time: {data['end']}</p>\n"
    html += f"<p>Total Checks: {data['checks']}</p>\n"
    html += f"<p>Score: {data['score']}</p>\n"

    # Agregar resultados de las pruebas
    html += "<h2>Test Results</h2>\n"
    for test in data["tests"]:
        html += f"<h3>{test['desc']}</h3>\n"
        html += "<ul>\n"
        for result in test["results"]:
            html += f"<li>{result['desc']}: {result['result']}</li>\n"
            if "details" in result:
                html += f"<p>{result['details']}</p>\n"
        html += "</ul>\n"

    html += "</body>\n</html>"

    output_name = output_file
    # Guardar el HTML en un archivo
    with open(output_name, "w") as file:
        file.write(html)

    print(f"Se ha generado el archivo HTML: {output_name}")

json2html("docker-bench_output.json", "docker_bench_report.html")
