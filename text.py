
Public Sub 计算()

Dim rng As Range, num As Long
For Each rng In Range([c2], [c2].End(xlDown))
    Dim text As String
    text = rng.Value: Rem 取值
    Rem --字符串处理
    leng = Len(text)
    Dim currentRange As Range
    Rem --遍历字符串
    Dim chars As String
    For i = 1 To leng
        Dim char As String
        char = Mid(a, i, 1)
        If Asc(char) >= 40 And Asc(char) <= 57 And Asc(char) <> 44 Then
            chars = chars + char
            End If
        If Asc(char) = 61 Then
            Exit For
            End If
    Rem Next i
    rng.Offset(0, -1).Value = chars
Next


End Sub