


def update_userprofile(instance, validated_data, profile_data):
    telegram_id = profile_data.get('telegram_id')
    facilities = profile_data.get('facilities')
    company = validated_data.get('company')
    avatar = profile_data.get('avatar')
    print(avatar)
    profile = instance
    if facilities:
        for facilities in facilities:
            profile.facilities.add(facilities)
    else:
        profile.facilities.clear()
    if company:
        profile.company = company
    else:
        profile.company.clean()
    if profile_data:
        profile.telegram_id = telegram_id
    if avatar:
        profile.avatar = avatar
    profile.save()
    return instance

