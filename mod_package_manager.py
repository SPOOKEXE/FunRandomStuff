
from dataclasses import dataclass

CACHE_DIRECTORY = 'mod_cache'

@dataclass
class ModInfo:
	unique_id : int
	name : str
	version : str

def find_mod_file( mod_info : ModInfo ) -> str:
	pass

def download_mod_file( mod_info : ModInfo ) -> tuple[bool, str]:
	pass

if __name__ == '__main__':

	v1_mod = ModInfo(  )
