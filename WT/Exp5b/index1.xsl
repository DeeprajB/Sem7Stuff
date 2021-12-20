<xsl:stylesheet version = "1.0" xmlns:xsl ="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/books">
<html>
<style>
table, th, td {
border: 1px solid black;
}
th{
color:grey;
}
.author{
text-transform:uppercase;
font-weight:bold;
color:blue;
}
</style>
<body>
<table>
<tr>
<th>Title</th>
<th>Author</th>
<th>Publisher</th>
<th>Year First Published</th>
</tr>
<xsl:for-each select="book">
<tr>
<td><xsl:value-of select="title"/></td>
<td class="author"><xsl:value-of select="author"/></td>
<td><xsl:value-of select="publisher"/></td>
<td><xsl:value-of select="year"/></td>
</tr>
</xsl:for-each>
</table>
</body>
</html>
</xsl:template>
</xsl:stylesheet>