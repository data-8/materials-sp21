test = {
  'name': 'q61',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(collection_times) == np.ndarray
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(collection_times)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> all(collection_times == np.arange(0, 31*24*60*60, 60*60))
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
