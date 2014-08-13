# -*- coding: Latin-1 -*-
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See License.txt for complete terms.

# IMAGE_SECTION_HEADER -> CybOX Windows Executable File Object Section Header Struct mappings
IMAGE_SECTION_HEADER_MAPPINGS = {'Name':'sections/section_header/name',
                                 'Misc_VirtualSize':'section/section_header/virtual_size',
                                 'VirtualAddress':'sections/section_header/virtual_address',
                                 'SizeOfRawData':'sections/section_header/size_of_raw_data',
                                 'PointerToRawData':'sections/section_header/pointer_to_raw_data',
                                 'PointerToRelocations':'sections/section_header/pointer_to_relocations',
                                 'PointerToLinenumbers':'sections/section_header/pointer_to_linenumbers',
                                 'NumberOfRelocations':'sections/section_header/number_of_relocations',
                                 'NumberOfLinenumbers':'sections/section_header/number_of_linenumbers',
                                 'Characteristics':'sections/section_header/characteristics'}