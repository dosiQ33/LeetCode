int strStr(char* haystack, char* needle) {
    int i = 0, j = 0, k = 0, l;
    
    if (*needle == '\0')
        return 0;
	int lenh = strlen(haystack);
	int lenn = strlen(needle);

	while (haystack[i] != '\0')
	{
	    if (haystack[i] == needle[j])
	    {
	        j++;
	        l = i;
	    }
	    else
	    {
	    	if (j > 0)
	    		i = i - j;
	        j = 0;
	    }
	    if (j == lenn)
	    {
	    	k = 1;
	    	i = lenh - 1;
	    }
	    i++;
	}
    if (k == 1)
    	return (l - j + 1);
    else
    	return (-1);
}
