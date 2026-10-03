# Joverlay

Simple text overlay application. 

Displays automatically on top of windowed and borderless applications.

# How to run

On Windows, use start.cmd.

Otherwise, run:

```
uv run app.py
```

# How to use

Click the widget to focus, and then copy-paste your content in.

Press Alt + Left Mouse Button to move the widget.

# How to configure

Apply position, size and CSS styles in configuration.json (root directory, same level as app.py).

Configuration file is not mandatory. Defaults to small size with black background.

For example:

```
{
  "x": 100,
  "y": 100,
  "width": 400,
  "height": 400,
  "background-color": "rgba(0, 0, 0, 200)",
  "text-color": "rgba(255, 255, 255, 255)",
  "font-size": "16px"
}
```