#!/usr/bin/env python3
"""Serveur local autonome ; Python 3, sans dépendance à installer."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import argparse
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--port',type=int,default=8766)
args=parser.parse_args()
root=Path(__file__).resolve().parent
handler=partial(SimpleHTTPRequestHandler,directory=str(root))
with ThreadingHTTPServer(('127.0.0.1',args.port),handler) as server:
    print(f'Dossier : {root}\nOuvrir http://localhost:{args.port}/',flush=True)
    try: server.serve_forever()
    except KeyboardInterrupt: pass
