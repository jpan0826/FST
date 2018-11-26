# Ju Pan

import fst


class Parser():

	def __init__(self):
		pass

	def generate(self, analysis):
		"""Generate the morphologically correct word 

		e.g.
		p = Parser()
		analysis = ['p','a','n','i','c','+past form']
		p.generate(analysis)
		---> 'panicked'
		"""
		f1 = fst.FST('generator')
		f1.add_state('start')
		f1.add_state('a1')
		f1.add_state('a2')
		f1.add_state('a3')
		f1.add_state('b1')
		f1.add_state('b2')
		f1.add_state('b3')
		f1.add_state('c1')
		f1.add_state('c2')
		f1.add_state('c3')
		f1.add_state('c4')
		f1.add_state('d1')
		f1.add_state('d2')
		f1.add_state('d3')
		f1.add_state('d4')
		f1.add_state('e1')
		f1.add_state('e2')
		f1.add_state('e3')
		f1.add_state('insertion')
		f1.add_state('progressive')
		f1.add_state('past')
		f1.add_state('end')
		f1.initial_state = 'start'
		f1.set_final('end')

		f1.add_arc('start', 'a1', 'w', 'w')
		f1.add_arc('a1', 'a2', 'a', 'a')
		f1.add_arc('a2', 'a3', 'n', 'n')
		f1.add_arc('a3', 'past', 't', 't')
		f1.add_arc('a3', 'progressive', 't', 't')

		f1.add_arc('start', 'b1', 's', 's')
		f1.add_arc('b1', 'b2', 'y', 'y')
		f1.add_arc('b2', 'b3', 'n', 'n')
		f1.add_arc('b3', 'past', 'c', 'c')
		f1.add_arc('b3', 'progressive', 'c', 'c')

		f1.add_arc('start', 'c1', 'p', 'p')
		f1.add_arc('c1', 'c2', 'a', 'a')
		f1.add_arc('c2', 'c3', 'n', 'n')
		f1.add_arc('c3', 'c4', 'i', 'i')
		f1.add_arc('c4', 'insertion', 'c', 'c')
		f1.add_arc('insertion', 'past', '', 'k')
		f1.add_arc('insertion', 'progressive', '', 'k')

		f1.add_arc('start', 'd1', 'h', 'h')
		f1.add_arc('d1', 'd2', 'a', 'a')
		f1.add_arc('d2', 'd3', 'v', 'v')
		f1.add_arc('d3', 'd4', 'o', 'o')
		f1.add_arc('d4', 'insertion', 'c', 'c')

		f1.add_arc('start', 'e1', 'l', 'l')
		f1.add_arc('e1', 'e2', 'i', 'i')
		f1.add_arc('e2', 'e3', 'c', 'c')
		f1.add_arc('e3', 'past', 'k', 'k')
		f1.add_arc('e3', 'progressive', 'k', 'k')


		f1.add_arc('past', 'end', '+past form', 'ed')
		f1.add_arc('progressive', 'end', '+present participle', 'ing')


		# output = ['p','a','n','i','c','k','e','d']
		# return ''.join(output)
		#print(f1.transduce(analysis))
		return ''.join(f1.transduce(analysis)[0])

	def parse(self, word):
		"""Parse a word morphologically 

		e.g.
		p = Parser()
		word = ['p', 'a', 'n', 'i', 'c', 'k','e','d']
		p.parse(word)
		---> 'panic+past form'
		"""
		f2 = fst.FST('parser')

		f2.add_state('start')
		f2.add_state('a1')
		f2.add_state('a2')
		f2.add_state('a3')
		f2.add_state('b1')
		f2.add_state('b2')
		f2.add_state('b3')
		f2.add_state('c1')
		f2.add_state('c2')
		f2.add_state('c3')
		f2.add_state('c4')
		f2.add_state('d1')
		f2.add_state('d2')
		f2.add_state('d3')
		f2.add_state('d4')
		f2.add_state('e1')
		f2.add_state('e2')
		f2.add_state('e3')
		f2.add_state('deletion')
		f2.add_state('progressive1')
		f2.add_state('progressive2')
		f2.add_state('progressive3')
		f2.add_state('past1')
		f2.add_state('past2')
		f2.add_state('end')
		f2.initial_state ='start'
		f2.set_final('end')

		f2.add_arc('start', 'a1', 'w', 'w')
		f2.add_arc('a1', 'a2', 'a', 'a')
		f2.add_arc('a2', 'a3', 'n', 'n')
		f2.add_arc('a3', 'past1', 't', 't')
		f2.add_arc('a3', 'progressive1', 't', 't')

		f2.add_arc('start', 'b1', 's', 's')
		f2.add_arc('b1', 'b2', 'y', 'y')
		f2.add_arc('b2', 'b3', 'n', 'n')
		f2.add_arc('b3', 'past1', 'c', 'c')
		f2.add_arc('b3', 'progressive1', 'c', 'c')

		f2.add_arc('start', 'c1', 'p', 'p')
		f2.add_arc('c1', 'c2', 'a', 'a')
		f2.add_arc('c2', 'c3', 'n', 'n')
		f2.add_arc('c3', 'c4', 'i', 'i')
		f2.add_arc('c4', 'deletion', 'c', 'c')
		f2.add_arc('deletion', 'past1', 'k', '')
		f2.add_arc('deletion', 'progressive1', 'k', '')

		f2.add_arc('start', 'd1', 'h', 'h')
		f2.add_arc('d1', 'd2', 'a', 'a')
		f2.add_arc('d2', 'd3', 'v', 'v')
		f2.add_arc('d3', 'd4', 'o', 'o')
		f2.add_arc('d4', 'deletion', 'c', 'c')

		f2.add_arc('start', 'e1', 'l', 'l')
		f2.add_arc('e1', 'e2', 'i', 'i')
		f2.add_arc('e2', 'e3', 'c', 'c')
		f2.add_arc('e3', 'past1', 'k', 'k')
		f2.add_arc('e3', 'progressive1', 'k', 'k')

		f2.add_arc('past1', 'past2', 'e', '+')
		f2.add_arc('past2', 'end', 'd', 'past form')

		f2.add_arc('progressive1', 'progressive2', 'i', '+')
		f2.add_arc('progressive2', 'progressive3', 'n', '')
		f2.add_arc('progressive3', 'end', 'g', 'present participle')

		# output = ['p','a','n','i','c','+past form']
		# return ''.join(output)
		return ''.join(f2.transduce(word)[0])
