from config.db_config import create_db_connection

def get_transit_schedule_dao(origin_station_id, destination_station_id, page, per_page):
    connection = create_db_connection()
    cursor = connection.cursor(dictionary=True)

    offset = (page - 1) * per_page

    query = """
    SELECT transit_mode, estimated_arrival_origin, estimated_arrival_destination
    FROM train_schedule
    WHERE origin_station_id = %s AND destination_station_id = %s
    ORDER BY estimated_arrival_origin
    LIMIT %s OFFSET %s
    """

    cursor.execute(query, (origin_station_id, destination_station_id, per_page, offset))
    schedules = cursor.fetchall()

    for schedule in schedules:
        schedule['estimated_arrival_origin'] = str(schedule['estimated_arrival_origin'])
        schedule['estimated_arrival_destination'] = str(schedule['estimated_arrival_destination'])

    cursor.close()
    connection.close()

    return schedules
