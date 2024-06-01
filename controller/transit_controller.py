from flask import Blueprint, request, jsonify
from service.transit_service import get_transit_schedule_service


transit_schedule_bp = Blueprint('transit_schedule', __name__)

@transit_schedule_bp.route('/schedule', methods=['GET'])
def get_transit_schedule():
    origin_station_id = request.args.get('origin_station_id')
    destination_station_id = request.args.get('destination_station_id')

    if not origin_station_id:
        return jsonify({'error': 'origin_station_id is required'}), 400

    if not destination_station_id:
        return jsonify({'error': 'destination_station_id is required'}), 400

    try:
        page = int(request.args.get('page', 1))
    except ValueError:
        return jsonify({'error': 'Invalid value for page'}), 400

    try:
        per_page = int(request.args.get('per_page', 10))
    except ValueError:
        return jsonify({'error': 'Invalid value for per_page'}), 400

    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')

    response = get_transit_schedule_service(
        origin_station_id, destination_station_id, latitude, longitude, page, per_page
    )
    return jsonify(response)
