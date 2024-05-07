"""Main module."""
import ipyleaflet

class Map(ipyleaflet.Map()):
    
    def __init__(self,center=(-10, 35 ), zoom=5,  **kwargs):
        super()__init__(center=center, zoom=zoom, **kwargs) # type: ignore
        self.add_control(ipyleaflet.LayersControl())