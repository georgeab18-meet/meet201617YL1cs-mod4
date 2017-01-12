#FIX THE LINE BELOW
class MyStr(str) : #<-----Replace xyz-make a new class, MyStr, that inherits from str
    """
    Build a subclass of str with some new, fun methods.
    """
    #The first method is done for you; you must complete the second (replace).
    
    def exclaim(self,num):
        """
        Add num exclamation points to string.
        (We did this example in class.)

        :param num: number of exclamation points to add
        :returns: a string with num exclamation points added to the end
        """
        return self+'!'*num

    def replace(self, take_out, use_this):
        """
        Override the replace method of string.
        The new replace method is case-insensitive,
        and the output will always be lower-case.

        Examples:
        >>> test=MyStr('aAaA')
        >>> test.replace('a','b')
        bbbb

        >>> test=MyStr('aAaADD')
        >>> test.replace('AA','c')
        ccdd

        :param take_out: the substring that will be replaced
        :param use_this: the substring that will be used in place of take_out

        :returns: a new string with replacement complete
        """
        #################
        #Make this method work in the way described in
        #the block comment above.
        #Hints:
        # 1. Remember that self is a MyStr object,
        #    and a MyStr object is also a str.
        #    However, remember that to call the replace
        #    method of str, you may need to use super
        # 2. The following str methods will be helpful:
        #       replace, lower, and upper
        # 3. There are multiple solutions, but you can
        #       do this in as little as 1 line.
        #YOUR CODE BELOW:
        #################
        String = self.lower()
        TAKE_OUTc = take_out.lower()
        use_it = use_this.lower()
        return str(String).replace(TAKE_OUTc,use_it)
    
        
