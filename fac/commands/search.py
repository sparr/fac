from fac.commands import Command, Arg


class SearchCommand(Command):
    'Search the mods database.'

    name = 'search'

    arguments = [
        Arg('query', help='search string', nargs='?'),

        Arg('-t', help='filter by tag', nargs='*', dest='tag', default=[]),

        Arg('-d', help='sort results by most downloaded',
            action='store_const',
            dest='sort',
            const='top',
            default='top'),

        Arg('-a', help='sort results alphabetically',
            action='store_const',
            dest='sort',
            const='alpha'),

        Arg('-u', help='sort results by most recently updated',
            action='store_const',
            dest='sort',
            const='updated'),

        Arg('-l', '--limit', type=int,
            help='only show that many results'),
    ]

    def run(self, args):
        for result in self.api.search(
                query=args.query or '',
                tags=tuple(args.tag),
                order=args.sort,
                limit=args.limit):

            if result.tags:
                tags = ' [%s]' % (', '.join(tag.name for tag in result.tags))
            else:
                tags = ''

            print('%s (%s)%s\n    %s\n' % (
                result.title, result.name,
                tags,
                result.summary.replace('\n', '')))
