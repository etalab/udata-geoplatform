# uData Geoplatform connector

Connects uData with Geoplatform (geo.data.gouv.fr)

## Usage

Install the plugin package in you udata environement:

```bash
pip install udata-geoplatform
```

Then activate it in your `udata.cfg`:

```python
PLUGINS = ['geoplatform']
```

## Configuration

You can control this plugin’s behavior with the following `udata.cfg` parameters:

- **`GEOPLATFORM_URL`**: The URL to your `geoplatform` instance (without trailing slash). **ex:** `https://geo.data.gouv.fr`
