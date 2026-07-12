import os
import logging
from flask import Flask, send_from_directory, jsonify
import yaml

app = Flask(__name__, static_folder='.', static_url_path='')


def load_profile():
	"""Load profile data from arun.yml next to this script."""
	base = os.path.dirname(__file__)
	path = os.path.join(base, 'arun.yml')
	try:
		with open(path, 'r', encoding='utf-8') as f:
			return yaml.safe_load(f)
	except FileNotFoundError:
		app.logger.warning('arun.yml not found at %s', path)
		return {}
	except Exception:
		app.logger.exception('Failed to load arun.yml')
		return {}


@app.route('/')
def index():
	return send_from_directory('.', 'index.html')


@app.route('/api/profile')
def profile():
	data = load_profile()
	if not data:
		return jsonify({'error': 'profile not found'}), 404
	return jsonify(data)


@app.route('/health')
def health():
	return jsonify({'status': 'ok'})


if __name__ == '__main__':
	logging.basicConfig(level=logging.INFO)
	port = int(os.environ.get('PORT', 5000))
	app.logger.info('Starting app on port %s', port)
	app.run(host='0.0.0.0', port=port, debug=True)

