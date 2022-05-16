from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic
from .models import Book, BookInstance, Author, Genre


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(
        status__exact='a').count()
    num_authors = Author.objects.count()
    num_genre = Genre.objects.all().count()
    num_rings_title_book = Book.objects.filter(
        title__icontains="rings").count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(
        request,
        'index.html',
        context={
            'num_books': num_books,
            'num_instances': num_instances,
            'num_instances_available': num_instances_available,
            'num_authors': num_authors,
            'num_genre': num_genre,
            'num_rings_title_book': num_rings_title_book,
            'num_visits': num_visits
        }
    )


class BookListView(generic.ListView):
    model = Book  # ваше собственное имя переменной контекста в шаблоне
    paginate_by = 2
    '''# context_object_name = "book_list"
    # template_name = 'books/book_list.html'
    # queryset = Book.objects.filter(title__icontains='war')[:5] Получение 5 книг, содержащих слово 'war' в заголовке

    # def get_context_data(self):
    #     context = super(BookListView, self).get_context_data(**kwargs)
    #     context['some_data'] = 'This is just some data'
    #     return context

    # def get_queryset(self):
    #     return Book.objects.filter(title__icontains='war')[:5]'''


class BookDetailViews(generic.DetailView):
    model = Book
    '''# def book_detail_view(request, pk):
    #     try:
    #         book_id = Book.objects.get(pk=pk)
    #     except Book.DoesNotExist:
    #         raise Http404("Book does not exist")

    #     return render(
    #         request,
    #         "catalog/book_detail.html",
    #         context={'book': book_id}
    #     )'''


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 2


class AuthorDetailView(generic.DetailView):
    model = Author


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
    

class LoanedAllBooksBorrowed(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_book.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o')
