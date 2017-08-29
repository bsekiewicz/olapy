CUBE = 'sales'

query1 = """
    SELECT
    Hierarchize({[Measures].[Amount]}) ON COLUMNS
    FROM [sales]
"""

query2 = """
    SELECT
    Hierarchize({[Geography].[Economy].[Partnership]}) ON COLUMNS
    FROM [sales]
"""

query3 = """
    SELECT
    Hierarchize(non empty {[Geography].[Geo].[Country].Members}) ON COLUMNS,
    Hierarchize({[Measures].[Amount]}) ON ROWS
    FROM [sales]
"""

query4 = """
    SELECT
    Hierarchize({[Geography].[Economy].[Partnership]}) ON COLUMNS,
    Hierarchize(non empty {[Geography].[Geo].[Country].Members}) ON ROWS
    FROM [sales]
"""

query5 = """
SELECT
    Hierarchize({[Geography].[Economy].[Partnership].[EU],
        [Geography].[Economy].[Partnership].[None],
        [Geography].[Economy].[Partnership].[NAFTA]}) ON COLUMNS,
    {[Product].[Prod].[Company].[Crazy Development],
    [Product].[Prod].[Company].[Company_test],
    [Product].[Prod].[Company].[test_Development]} ON ROWS
    FROM [sales]
"""

# GENERATED BY EXCEL
query6 = """
    SELECT NON EMPTY
    Hierarchize(AddCalculatedMembers(DrilldownMember({{DrilldownMember({{DrilldownMember({{
    [Time].[Time].[Year].Members}}, {
    [Time].[Time].[Year].[2010]})}}, {
    [Time].[Time].[Quarter].[2010].[Q2 2010]})}}, {
    [Time].[Time].[Month].[2010].[Q2 2010].[May 2010]}))) DIMENSION PROPERTIES PARENT_UNIQUE_NAME,HIERARCHY_UNIQUE_NAME
    ON COLUMNS
    FROM [sales]
    WHERE ([Measures].[Amount])
    CELL PROPERTIES VALUE, FORMAT_STRING, LANGUAGE, BACK_COLOR, FORE_COLOR, FONT_FLAGS
"""

query7 = """
    SELECT {(
    [Product].[Product].[Company].[Crazy Development],
    [Time].[Time].[Day].[2010].[Q2 2010].[May 2010].[May 18,2010],
    [Geography].[Geography].[Continent].[Europe],
    [Measures].[Amount]),

    ([Product].[Product].[Company].[Crazy Development],
    [Time].[Time].[Day].[2010].[Q2 2010].[May 2010].[May 16,2010],
    [Geography].[Geography].[Continent].[Europe],
    [Measures].[Amount]),

    ([Product].[Product].[Company].[Crazy Development],
    [Time].[Time].[Day].[2010].[Q2 2010].[May 2010].[May 14,2010],
    [Geography].[Geography].[Continent].[Europe],[Measures].[Amount]),

    ([Product].[Product].[Company].[Crazy Development],
    [Time].[Time].[Day].[2010].[Q2 2010].[May 2010].[May 12,2010],
    [Geography].[Geography].[Continent].[Europe],
    [Measures].[Amount]),

    ([Product].[Product].[Company].[Crazy Development],
    [Time].[Time].[Day].[2010].[Q2 2010].[May 2010].[May 13,2010],
    [Geography].[Geography].[Continent].[Europe],
    [Measures].[Amount]),
    ([Product].[Product].[Company].[Crazy Development],
    [Time].[Time].[Day].[2010].[Q2 2010].[May 2010].[May 15,2010],
    [Geography].[Geography].[Continent].[Europe],
    [Measures].[Amount]),

    ([Product].[Product].[Company].[Crazy Development],
    [Time].[Time].[Day].[2010].[Q2 2010].[May 2010].[May 17,2010],
    [Geography].[Geography].[Continent].[Europe],
    [Measures].[Amount]),

    ([Product].[Product].[Company].[Crazy Development],
    [Time].[Time].[Day].[2010].[Q2 2010].[May 2010].[May 19,2010],
    [Geography].[Geography].[Continent].[Europe],
    [Measures].[Amount]

    )} ON 0
    FROM [sales]
    CELL PROPERTIES VALUE, FORMAT_STRING, LANGUAGE, BACK_COLOR, FORE_COLOR, FONT_FLAGS

    """

query8 = """
    SELECT {(
    [Geography].[Geography].[Country].[Europe].[Spain],
    [Measures].[Amount]),

    ([Geography].[Geography].[Country].[Europe].[France],
    [Measures].[Amount]),

    ([Geography].[Geography].[Country].[Europe].[Switzerland],
    [Measures].[Amount])}

    ON 0
    FROM [sales]
    CELL PROPERTIES VALUE, FORMAT_STRING, LANGUAGE, BACK_COLOR, FORE_COLOR, FONT_FLAGS
"""

query9 = """
    SELECT
    {([Time].[Time].[Day].[2010].[Q2 2010].[May 2010].[May 19,2010],
    [Geography].[Geography].[Continent].[Europe],
    [Measures].[Amount]),

    ([Time].[Time].[Day].[2010].[Q2 2010].[May 2010].[May 17,2010],
    [Geography].[Geography].[Continent].[Europe],
    [Measures].[Amount]),

    ([Time].[Time].[Day].[2010].[Q2 2010].[May 2010].[May 15,2010],
    [Geography].[Geography].[Continent].[Europe],
    [Measures].[Amount]),

    ([Time].[Time].[Day].[2010].[Q2 2010].[May 2010].[May 13,2010],
    [Geography].[Geography].[Continent].[Europe],
    [Measures].[Amount]),

    ([Time].[Time].[Day].[2010].[Q2 2010].[May 2010].[May 12,2010],
    [Geography].[Geography].[Continent].[Europe],
    [Measures].[Amount]),

    ([Time].[Time].[Day].[2010].[Q2 2010].[May 2010].[May 14,2010],
    [Geography].[Geography].[Continent].[Europe],
    [Measures].[Amount]),

    ([Time].[Time].[Day].[2010].[Q2 2010].[May 2010].[May 16,2010],
    [Geography].[Geography].[Continent].[Europe],
    [Measures].[Amount]),

    ([Time].[Time].[Day].[2010].[Q2 2010].[May 2010].[May 18,2010],
    [Geography].[Geography].[Continent].[Europe],
    [Measures].[Amount])}

    ON 0
    FROM [sales]

    CELL PROPERTIES VALUE, FORMAT_STRING, LANGUAGE, BACK_COLOR, FORE_COLOR, FONT_FLAGS
"""

query10 = """
    SELECT {(
    [Time].[Time].[Day].[2010].[Q2 2010].[May 2010].[May 19,2010],
    [Geography].[Geography].[Continent].[Europe],
    [Measures].[Count]),

    ([Time].[Time].[Day].[2010].[Q2 2010].[May 2010].[May 17,2010],
    [Geography].[Geography].[Continent].[Europe],
    [Measures].[Count]),

    ([Time].[Time].[Day].[2010].[Q2 2010].[May 2010].[May 15,2010],
    [Geography].[Geography].[Continent].[Europe],
    [Measures].[Count]),

    ([Time].[Time].[Day].[2010].[Q2 2010].[May 2010].[May 13,2010],
    [Geography].[Geography].[Continent].[Europe],
    [Measures].[Count]),

    ([Time].[Time].[Day].[2010].[Q2 2010].[May 2010].[May 12,2010],
    [Geography].[Geography].[Continent].[Europe],
    [Measures].[Count]),

    ([Time].[Time].[Day].[2010].[Q2 2010].[May 2010].[May 14,2010],
    [Geography].[Geography].[Continent].[Europe],
    [Measures].[Count]),

    ([Time].[Time].[Day].[2010].[Q2 2010].[May 2010].[May 16,2010],
    [Geography].[Geography].[Continent].[Europe],
    [Measures].[Count]),

    ([Time].[Time].[Day].[2010].[Q2 2010].[May 2010].[May 18,2010],
    [Geography].[Geography].[Continent].[Europe],
    [Measures].[Count])}

    ON 0
    FROM [sales]
    CELL PROPERTIES VALUE, FORMAT_STRING, LANGUAGE, BACK_COLOR, FORE_COLOR, FONT_FLAGS
"""

where = "WHERE [Time].[Calendar].[Day].[May 12,2010]"

# TODO queries without
