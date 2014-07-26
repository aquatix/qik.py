from flask import Blueprint, render_template, session, redirect, url_for, \
    request, flash, g, jsonify, abort


mod = Blueprint('general', __name__)


@mod.route('/')
def index():
    if request_wants_json():
        return jsonify(releases=[r.to_json() for r in releases])
    return render_template('general/index.html',
                           latest_release=releases[-1])


@mod.route('/search/')
def search():
    q = request.args.get('q') or ''
    page = request.args.get('page', type=int) or 1
    results = None
    if q:
        results = perform_search(q, page=page)
        if results is None:
            abort(404)
    return render_template('general/search.html', results=results, q=q)


