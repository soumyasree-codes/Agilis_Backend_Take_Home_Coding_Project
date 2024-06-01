from dao.transit_dao import get_transit_schedule_dao

def get_transit_schedule_service(origin_station_id, destination_station_id, latitude, longitude, page, per_page):
    schedules = get_transit_schedule_dao(origin_station_id, destination_station_id, page, per_page)
    return {"next_schedules": schedules}
