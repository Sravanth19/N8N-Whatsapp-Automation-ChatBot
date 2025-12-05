# Troubleshooting Guide

This guide helps you resolve common issues with the WhatsApp n8n Chatbot.

## WhatsApp API Issues

### Webhook Not Receiving Messages

**Symptoms:**
- Messages sent to WhatsApp number don't trigger the chatbot
- n8n logs show no incoming webhooks

**Solutions:**
1. Verify webhook URL in WhatsApp Business API settings
2. Ensure the URL is HTTPS in production
3. Check verify token matches between WhatsApp and your configuration
4. Confirm n8n is running and accessible
5. Test webhook manually: `./scripts/test-webhook.sh <webhook_url>`

### Invalid Access Token

**Symptoms:**
- API calls return 401 Unauthorized
- Messages fail to send

**Solutions:**
1. Regenerate access token in Facebook Developers console
2. Update `WHATSAPP_ACCESS_TOKEN` in your environment variables
3. Ensure token hasn't expired (temporary tokens last 24 hours)
4. Request permanent token for production use

### Phone Number Not Verified

**Symptoms:**
- Phone number shows as unverified in WhatsApp Business API

**Solutions:**
1. Complete phone number verification in Facebook Developers
2. Ensure the number is in international format
3. Wait for verification SMS and enter the code
4. Check that the number is eligible for WhatsApp Business

## n8n Issues

### Workflow Not Executing

**Symptoms:**
- Webhook receives data but workflow doesn't run
- No executions visible in n8n logs

**Solutions:**
1. Ensure workflow is active (green play button)
2. Check webhook path matches exactly
3. Verify node connections are correct
4. Check for errors in workflow execution log
5. Test individual nodes manually

### OpenAI Integration Failing

**Symptoms:**
- Chat responses are empty or error messages appear
- OpenAI API calls fail

**Solutions:**
1. Verify `OPENAI_API_KEY` is set correctly
2. Check API key has sufficient credits
3. Ensure correct model is selected (gpt-3.5-turbo or gpt-4)
4. Check rate limits haven't been exceeded
5. Verify message format in the workflow

### Port Already in Use

**Symptoms:**
- n8n fails to start with "port already in use" error

**Solutions:**
1. Change port: `n8n --port 5679`
2. Find process using port: `lsof -i :5678` (Linux/Mac) or `netstat -ano | findstr :5678` (Windows)
3. Kill conflicting process or use different port
4. Update webhook URLs accordingly

## Network and Connectivity

### Firewall Blocking Connections

**Symptoms:**
- Unable to access n8n web interface
- Webhook calls fail

**Solutions:**
1. Check firewall settings allow port 5678
2. For Docker, ensure container networking is configured
3. Verify host machine can reach localhost/127.0.0.1
4. Check VPN or proxy settings

### HTTPS Certificate Issues

**Symptoms:**
- Browser shows certificate warnings
- WhatsApp rejects webhook URL

**Solutions:**
1. Obtain valid SSL certificate (Let's Encrypt for free)
2. Configure reverse proxy (nginx) with SSL
3. Update webhook URL to use HTTPS
4. Ensure certificate chain is complete

## Environment Configuration

### Environment Variables Not Loading

**Symptoms:**
- Configuration values are undefined
- API calls fail with missing parameters

**Solutions:**
1. Ensure `.env` file exists in correct location
2. Check file permissions allow reading
3. Verify variable names match exactly (case-sensitive)
4. Restart n8n after changing environment variables
5. Use absolute paths if needed

### Python Script Errors

**Symptoms:**
- `send-message-example.py` fails to run
- Import errors or missing dependencies

**Solutions:**
1. Install required packages: `pip install requests python-dotenv`
2. Ensure Python 3.6+ is installed
3. Check environment variables are loaded
4. Verify file permissions are executable
5. Run with: `python3 scripts/send-message-example.py`

## Performance Issues

### Slow Response Times

**Symptoms:**
- Chatbot takes long time to respond
- OpenAI API calls timeout

**Solutions:**
1. Check internet connection speed
2. Monitor OpenAI API usage and limits
3. Optimize workflow (remove unnecessary nodes)
4. Consider upgrading to paid OpenAI plan
5. Implement caching for frequent responses

### High Memory Usage

**Symptoms:**
- n8n consumes excessive RAM
- System becomes slow or unresponsive

**Solutions:**
1. Limit workflow executions
2. Clean up old execution logs
3. Use external database instead of SQLite
4. Monitor and restart n8n periodically
5. Upgrade server resources

## Logs and Debugging

### Enabling Debug Logging

```bash
# Set log level
export N8N_LOG_LEVEL=debug

# Restart n8n
```

### Checking Logs

- n8n web interface: Executions > View logs
- Docker: `docker logs n8n`
- File system: Check `~/.n8n/logs/` directory

### Common Log Messages

- **"Webhook received"**: Good, webhook is working
- **"Invalid signature"**: Verify token mismatch
- **"Rate limit exceeded"**: Slow down API calls
- **"Model not found"**: Check OpenAI model name

## Getting Help

If issues persist:

1. Check the [n8n Documentation](https://docs.n8n.io/)
2. Review [WhatsApp Business API Docs](https://developers.facebook.com/docs/whatsapp/)
3. Search GitHub issues for similar problems
4. Post on n8n community forums
5. Check system requirements and compatibility

## Preventive Measures

- Regularly update n8n and dependencies
- Monitor API usage and costs
- Backup workflows and configurations
- Test changes in development environment first
- Keep API keys secure and rotate regularly
