<?xml version="1.0"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:output method="html"/>
<xsl:template match="/">
<html>
<head>
<title>thesaurus.xsl</title>
</head>
<body style="background-color:powderblue;"> 
<h1 style="text-align:center;color:red">IWP EXPERIMENT - 11.(ii)</h1> 
<h1 style="text-align:center;color:red">18BCE0172 - AYUSH SHARMA</h1> 
<h1 style="text-align:center;color:red">THESAURUS SEARCH TOOL</h1> 
<form method="post" action="">
<table style="border:1px solid black;margin-left:auto;margin-right:auto;">
<tr>
<td>Enter word:</td>
</tr>
<tr>
<td><input type="text" id="search"/></td>
<td><input type="submit" id="submit" value="Submit"/></td>
</tr>
<xsl:variable name="SearchWord" select="umbraco.library:Request('submit')" />
<xsl:for-each select="theresa/word">
<xsl:if test="@content=$SearchWord">
<tr>
<td>ENTERED WORD: $SearchWord </td>
</tr>
<tr>
<td>Synonyms:- </td>
</tr>
<tr>
<td>
<xsl:value-of select="synonyms"/>
</td>
</tr>
 <tr>
<td>Antonyms:- </td>
</tr>
<tr>
<td>
<xsl:value-of select="antonyms"/>
</td>
</tr>
</xsl:if>
</xsl:for-each>
</table>
</form>
</body>
</html>
</xsl:template>
</xsl:stylesheet>
