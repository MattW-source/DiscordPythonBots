@Bot.command(client)
async def ban(ctx):
    '''
    Ban a member from a guild
    Usage: !ban <mention> {reason}

    '''
    if "rolename" in [role.name for role in ctx.author.roles]:
        args = ctx.message.content.split()
        if len(args) < 2: #No user given
            await ctx.send("Invalid Usage; Usage: `!ban <mention> {reason}")
        else:
            if len(args) < 3: #No reason provided
                reason = "No Reason"
            else:
                reason = " ".join(args[2:]) #Join the args to create the reason string
            offender = discord.utils.get(ctx.guild.members, mention=args[1])
            await offender.ban(reason=reason) #Ban the specified member from the guild
            await ctx.send("Successfully Banned %s" % (offender.name))
    else:
        await ctx.send("You do not have permission for this")
