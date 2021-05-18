import re

def html_to_text(html, headers_max_words_count):
	
	html_regex = re.compile(re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});'))
	text = re.sub(html_regex, ' ', html)
	
	def do_grammatical_replaces(text):

		def do_full_replace(text, first, second):
			while first in text:
				text = text.replace(first, second)
			return text

		text = do_full_replace(text, '  ', ' ')
		text = do_full_replace(text, ' ,', ',')
		text = do_full_replace(text, ' !', '!')
		text = do_full_replace(text, ' ?', '?')
		text = do_full_replace(text, ' .', '.')
		text = do_full_replace(text, '( ', '(')
		text = do_full_replace(text, ' )', ')')
		text = do_full_replace(text, ' /', '/')
		text = do_full_replace(text, '/ ', '/')
		text = do_full_replace(text, '\n ', '\n')
		text = do_full_replace(text, ' \n', '\n')
		text = do_full_replace(text, '\n\n', '\n')

		return text

	text = text.replace('\r', '')
	text = do_grammatical_replaces(text)
	
	def remove_first(text, what):
		while text[:len(what)] == what:
			text = text[len(what):]
		return text

	text = remove_first(text, ' ')
	text = remove_first(text, '\n')

	text_to_join = []
	text_splitted = text.split('\n')
	for text_part in text_splitted:
		if text_part:
			text_part_splitted = text_part.split(' ')
			if len(text_part_splitted) <= headers_max_words_count:
				text_to_join.append('\n\n' + text_part + '\n')
			else:
				text_to_join.append(text_part)
		else:
			text_to_join.append(text_part)
	text = '\n'.join(text_to_join)
	if text[:4] == '\n\n':
		text = text[4:]

	return text
