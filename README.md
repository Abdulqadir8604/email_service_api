#### email_service_api
# LAMAQ EMAILER

### form implementation
```html
<form action="https://lamaq-emailer.vercel.app/send" method="post">
    <label>
        Email:<br>
        <input type="email" name="email" required>
    </label><br>
    <label>
        Subject:<br>
        <input type="text" name="subject" required>
    </label><br>
    <label>
        Body:<br>
        <input type="text" name="body" required>
    </label><br>

  <input type="submit" value="Submit">
</form>
```

### GET api
```/email/email={}&subject={}/body={}```


