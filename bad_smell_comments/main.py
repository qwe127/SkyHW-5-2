# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:
    # ...
    def move(self, field, field_x, field_y, direction, fly, crawl, points_per_action=1):
        if fly and crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        if fly:
            points_per_action *= 1.2
            if direction == 'UP':
                new_y = field_y + points_per_action
                new_x = field_x
            elif direction == 'DOWN':
                new_y = field_y - points_per_action
                new_x = field_x
            elif direction == 'LEFT':
                new_y = field_y
                new_x = field_x - points_per_action
            elif direction == 'RIGHT':
                new_y = field_y
                new_x = field_x + points_per_action

        if crawl:
            points_per_action *= 0.5
            if direction == 'UP':
                new_y = field_y + points_per_action
                new_x = field_x
            elif direction == 'DOWN':
                new_y = field_y - points_per_action
                new_x = field_x
            elif direction == 'LEFT':
                new_y = field_y
                new_x = field_x - points_per_action
            elif direction == 'RIGHT':
                new_y = field_y
                new_x = field_x + points_per_action

            field.set_unit(x=new_x, y=new_y, unit=self)
