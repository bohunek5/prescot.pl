with open("dystrybucja/index.html", "r") as f:
    text = f.read()

start = text.find('<div data-elementor-type="wp-page"')
end = text.find('</div><!-- #content -->')

print("Dystrybucja wp-page content length:", len(text[start:end]))
