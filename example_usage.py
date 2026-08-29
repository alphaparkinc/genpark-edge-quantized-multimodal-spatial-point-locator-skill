from client import EdgeQuantizedMultimodalSpatialPointLocatorClient

def main():
    client = EdgeQuantizedMultimodalSpatialPointLocatorClient()
    res = client.predict_point_coordinates('https://assets.genpark.ai/images/cockpit_instrument_panel.png', 'Point to altimeter and horizon indicator')
    print('Edge VLM Point Session: ' + res['point_session_id'] + ' (Format: ' + res['quantization_format'] + ')')
    print('Memory Footprint: ' + str(res['inference_memory_mb']) + ' MB | Hit Rate: ' + str(res['coordinate_hit_rate_pct']) + '%)')
    for pt in res['predicted_points']:
        print('  - ' + pt['label'] + ' -> (' + str(pt['x_pct']) + '%, ' + str(pt['y_pct']) + '%)')

if __name__ == '__main__':
    main()
