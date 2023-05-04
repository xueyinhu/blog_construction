# 将 JSON 数据解析为 HTML 内容
def parse_json_to_html(data, template_path):
    with open(template_path, 'r', encoding='utf-8') as f:
        html = f.read()
        html = html.replace('@title', data['title'])
        print(html)


data = {
    'title': 'test_column_title',
    'texts': [],
    'images': [],
    'columns': []
}
parse_json_to_html(data, './template/test_a/template.html')

