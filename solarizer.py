from flask import Flask, render_template, send_from_directory
app = Flask(__name__)

@app.route('/')
def index():
  names = ["base03", "base02", "base01", "base00", "base0", "base1", "base2", "base3",
    "yellow", "orange", "red", "magenta", "violet", "blue", "cyan", "green"] 
  
  help = {
    "base03": "dark background",
    "base02": "dark background highlight",
    "base01": "dark comments/secondary content<br>light optional emphasized content",
    "base00": "light body text/default code/primary content",
    "base0": "dark body text/default code/primary content",
    "base1": "dark optional emphasized content<br>light comments/secondary content",
    "base2": "light background highlight",
    "base3": "light background"
  }

  solarized_colors = ["002b36", "073642", "586e75", "657b83", "839496", "93a1a1", "eee8d5", "fdf6e3",
    "b58900", "cb4b16", "dc322f", "d33682", "6c71c4", "268bd2", "2aa198", "859900"]
  return render_template('index.html', colors=solarized_colors, names=names, help=help)

#probably not needed since the colorpicker change
@app.route('/<path:filename>')  
def send_file(filename):  
  return send_from_directory('static', filename)

if __name__ == '__main__':
  app.run(debug=True)
