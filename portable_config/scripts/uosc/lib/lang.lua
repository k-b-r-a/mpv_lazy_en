-- 导入上游 intl.lua 的部分函数
local locale = {}
local cache = {}
function get_languages()
	local languages = {}

	for _, lang in ipairs(comma_split(options.languages)) do
		if (lang == 'slang') then
			local slang = mp.get_property_native('slang')
			if slang then
				itable_append(languages, slang)
			end
		else
			languages[#languages +1] = lang
		end
	end

	return languages
end
---@param path string
function get_locale_from_json(path)
	local expand_path = mp.command_native({'expand-path', path})

	local meta, meta_error = utils.file_info(expand_path)
	if not meta or not meta.is_file then
		return nil
	end

	local json_file = io.open(expand_path, 'r')
	if not json_file then
		return nil
	end

	local json = json_file:read('*all')
	json_file:close()

	local json_table = utils.parse_json(json)
	return json_table
end
---@param text string
function t(text, a)
	if not text then return '' end
	local key = text
	if a then key = key .. '|' .. a end
	if cache[key] then return cache[key] end
	cache[key] = string.format(locale[text] or text, a or '')
	return cache[key]
end


ulang = {

    -- context_menu_default
    _cm_load = 'Load',
    _cm_file_browser = '※ File Browser',
    _cm_import_sid = '※ Import Subtitle Track',
    _cm_navigation = 'Navigation',
    _cm_playlist = '※ Playlist',
    _cm_edition_list = '※ Edition List',
    _cm_chapter_list = '※ Chapter List',
    _cm_vid_list = '※ Video Track List',
    _cm_aid_list = '※ Audio Track List',
    _cm_sid_list = '※ Subtitle Track List',
    _cm_playlist_shuffle = 'Shuffle Playlist',
    _cm_ushot = '※ Screenshot',
    _cm_video = 'Video',
    _cm_decoding_api = 'Toggle Decoding Mode',
    _cm_deband_toggle = 'Toggle Debanding',
    _cm_deint_toggle = 'Toggle Deinterlacing',
    _cm_icc_toggle = 'Toggle Auto Color Calibration',
    _cm_corpts_toggle = 'Toggle Timecode Parsing Mode',
    _cm_tools = 'Tools',
    _cm_keybinding = '※ Keybinding List',
    _cm_stats_toggle = 'Toggle Persistent Stats',
    _cm_console_on = 'Show Console',
    _cm_border_toggle = 'Toggle Window Border',
    _cm_ontop_toggle = 'Toggle Window On Top',
    _cm_audio_device = '※ Audio Output Device List',
    _cm_stream_quality = '※ Streaming Quality',
    _cm_show_file_dir = '※ Open Current File Directory',
    _cm_show_config_dir = '※ Open Configuration Directory',
    _cm_stop = 'Stop',
    _cm_quit = 'Quit mpv',

    -- no-border-title
    _border_title = 'No File Loaded',

    -- track_loaders sub_menu menu_data
    _sid_menu = 'Subtitle Track',
    _aid_menu = 'Audio Track',
    _vid_menu = 'Video Track',
    _import_id_menu = 'Import ',

    -- _menu_item_empty_title = 'Empty',
    _menu_search = 'Enter and press Ctrl+ENTER to search',
    _menu_search2 = 'Enter to search',

    _input_empty = 'input-bindings is empty',

    _sid_submenu_title = 'Subtitle Track List',
    _sid_sec_submenu_title = 'Secondary Subtitle Track List',
    _aid_submenu_title = 'Audio Track List',
    _vid_submenu_title = 'Video Track List',
    _playlist_submenu_title = 'Playlist',
    _chapter_list_submenu_title = 'Chapter List',
    _chapter_list_submenu_item_title = 'Unnamed Chapter ',
    _edition_list_submenu_title = 'Edition List',
    _edition_list_submenu_item_title = 'Edition',
    _stream_quality_submenu_title = 'Streaming Quality',
    _audio_device_submenu_title = 'Audio Output Device List',
    _audio_device_submenu_item_title = 'Auto',

    _dlsub_download = 'Download',
    _dlsub_searchol = 'Search Online',
    _dlsub_invalid_response = 'Invalid JSON Response',
    _dlsub_process_exit = 'Process Exit Code',
    _dlsub_unknown_err = 'Unknown Error',
    _dlsub_err = 'Error',
    _dlsub_fin = 'Download Complete and Loaded',
    _dlsub_remain = 'Remaining Downloads Today',
    _dlsub_reset = 'Reset',
    _dlsub_foreign = 'Foreign Parts Only',
    _dlsub_hearing = 'Hearing Impaired',
    _dlsub_result0 = 'No Results',
    _dlsub_page_prev = 'Previous Page',
    _dlsub_page_next = 'Next Page',
    _dlsub_2search = 'Ctrl+ENTER Search',
    _dlsub_enter_query = 'Enter Query',

    _submenu_import = 'Import',
    _submenu_load_file = 'Open File',
    _submenu_id_disabled = 'Disabled',
    _submenu_id_hint = 'Channel',
    _submenu_id_forced = 'Forced',
    _submenu_id_default = 'Default',
    _submenu_id_external = 'External',
    _submenu_id_title = 'Track ',
    _submenu_file_browser_item_hint = 'Drive List',
    _submenu_file_browser_item_hint2 = 'Parent Directory',
    _submenu_file_browser_item2_hint = 'Drive',
    _submenu_file_browser_title = 'Drive List',

    -- built-in_shortcut
    _button01 = 'Menu',
    _button02 = 'Subtitle Track',
    _button03 = 'Audio Track',
    _button04 = 'Audio Device',
    _button05 = 'Video Track',
    _button06 = 'Playlist',
    _button07 = 'Chapter',
    _button08 = 'Edition',
    _button09 = 'Stream Quality',
    _button10 = 'Load File',
    _button11 = 'Playlist/File Browser',
    _button12 = 'Previous',
    _button13 = 'Next',
    _button14 = 'First',
    _button15 = 'Last',
    _button16 = 'Loop List',
    _button17 = 'Loop Single',
    _button18 = 'Shuffle Playback',
    _button19 = 'Toggle Fullscreen',

    _button_ext01 = 'Play/Pause',
    _button_ext02 = 'Play/Pause',
    _button_ext03 = 'Previous',
    _button_ext04 = 'Next',
    _button_ext05 = 'Window Border',
    _button_ext06 = 'On Top',
    _button_ext07 = 'Hardware Decoding',
    _button_ext08 = 'Original Size',
    _button_ext09 = 'Debanding',
    _button_ext10 = 'Deinterlacing',
    _button_ext11 = 'Screenshot',
    _button_ext12 = 'Statistics',
    _button_ext13 = 'Timeline Preview',

}

opt.read_options(ulang, "uosc_lang")
