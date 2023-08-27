from config import *


def show_score(screen, font, snake):
    score = font.render("Score : "+str(snake.score), True, "#097969")
    score_rect = score.get_rect(centerx=WIDTH / 5, y=30)

    best = font.render("Best : "+str(snake.best_score), True, "#097969")
    best_rect = best.get_rect(centerx=WIDTH / 5 * 4, y=30)

    screen.blit(score, score_rect)
    screen.blit(best, best_rect)