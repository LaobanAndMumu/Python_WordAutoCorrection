"""
file: ritcs/mutable_str.py
language: python3

An attempt to imitate the Python str class for a string that can
be modified.
"""

__author__ = "James Heliotis"

__path__="."

from collections.abc import MutableSequence

class mutable_str( MutableSequence ):
    def __init__( self, data ):
        "Create a mutable_str from a str."
        self.data = list( data )

    def __repr__( self ):
        "Return a string that when evaluated recreates this object."
        return "mutable_str(\"" + "".join( self.data ) + "\")"

    def __str__( self ):
        "Return a string with the same contents as this object."
        return "".join( self.data )

    def __setitem__( self, index, value ):
        "Modify one of the characters using '[]'."
        self.data[ index ] = value

    def __getitem__( self, index ):
        "Retrieve one of the characters using '[]'."
        if type( index ) == slice:
            return mutable_str( self.data[ index ] )
        return self.data[ index ]

    def __delitem__( self, index ):
        "Delete a character from this string using 'del'."
        del self.data[ index ]

    def __add__( self, other ):
        """
        The concatenation operator '+'
        Works with str's and mutable_str's
        """
        result = mutable_str( self )
        result.data.extend( list( other ) )
        return result

    def __len__( self ):
        "Get the string length."
        return len( self.data )

    def __iter__( self ):
        "Allow this string's characters to be accessed via a for loop."
        return iter( self.data )

    def __eq__( self, other ):
        "The equality operator '=='"
        if type( other ) == str:
            return self.data == list( other )
        return self.data == other.data

    def __ne__( self, other ):
        "The inequality operator '!='"
        if type( other ) == str:
            return self.data != list( other )
        return self.data != other.data

    def __lt__( self, other ):
        "The less-than operator '<'"
        if type( other ) == str:
            return self.data < list( other )
        return self.data < other.data

    def __gt__( self, other ):
        "The greater-than operator '>'"
        if type( other ) == str:
            return self.data > list( other )
        return self.data > other.data

    def __le__( self, other ):
        "The less-than-or-equal operator '<='"
        if type( other ) == str:
            return self.data <= list( other )
        return self.data <= other.data

    def __ge__( self, other ):
        "The greater-than-or-equal operator '>='"
        if type( other ) == str:
            return self.data >= list( other )
        return self.data >= other.data

    def insert( self, index, value ):
        """
        Insert a new character into this string.
        :param index: the location before which the new character should go
        :param value: the new character
        :return: None
        """
        self.data.insert( index, value )


def test( ):
    print( "Starting test." )
    word = "fantabuloso"
    ms = mutable_str( word )
    assert repr( ms + 'h' ) == 'mutable_str("fantabulosoh")'
    assert [ c for c in ms ] == [ 'f','a','n','t','a','b','u','l','o','s','o' ]
    ms[1] = 'u'
    assert str(ms) == "funtabuloso"
    del ms[ 0 ]
    assert str(ms) == "untabuloso"
    assert ms[-2] == 's'
    mt = mutable_str( ms )
    assert str(mt) == "untabuloso"
    assert ms == mt
    assert not( mt is ms )
    assert not( mt < ms )
    assert not( mt < "alpha" )
    assert not( mt > ms )
    assert mt > "alpha"
    assert not( mt != ms )
    assert mt <= ms
    assert mt >= ms
    mt.insert( 4, 'i' )
    assert str(mt) == "untaibuloso"
    assert ms != mt
    assert not( mt is ms )
    assert not( mt < ms )
    assert not( mt < "alpha" )
    assert mt > ms
    assert mt > "alpha"
    assert not( mt == ms )
    assert not ( mt <= ms )
    assert mt >= ms
    print( "If you see this message, all the tests passed." )


if __name__ == '__main__':
    test( )