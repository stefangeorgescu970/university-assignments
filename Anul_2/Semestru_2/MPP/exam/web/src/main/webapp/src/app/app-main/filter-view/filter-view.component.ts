import {Component, OnInit} from '@angular/core';
import {Author} from '../shared/author.model';
import {Router} from '@angular/router';
import {AuthorService} from '../shared/author.service';
import {Book} from '../shared/book.model';
import {BookService} from '../shared/book.service';
import {BookWithData} from "../shared/bookWithData.model";

@Component({
  selector: 'app-filter-view',
  templateUrl: './filter-view.component.html',
  styleUrls: ['./filter-view.component.css'],
})

export class FilterViewComponent implements OnInit {
  errorMessage: string;
  books: Array<BookWithData>;
  authors: Array<Author>;
  yearValues = [2000, 2001, 2002, 2003, 2004, 2005];
  selectedAuthor = -1;
  selectedYear = -1;

  constructor(private authorService: AuthorService,
              private bookService: BookService,
              private router: Router) {

  }

  ngOnInit(): void {
      this.getBooks();
      this.getAuthors();
  }

  getBooks() {
    this.bookService.getBooks().subscribe(
      books => this.books = books,
      error => this.errorMessage = <any>error
    );
  }

  getAuthors() {
    this.authorService.getAuthors().subscribe(
      authors => this.authors = authors,
      error => this.errorMessage = <any>error
    );
  }

  public onChangeAuthor(event): void {
    const newVal = event.target.value;
    this.bookService.getBooksByAuthorAndYear(newVal, this.selectedYear).subscribe(
      books => this.books = books,
      error => this.errorMessage = <any>error
    );
  }

  public onChangeYear(event): void {
    const newVal = event.target.value;
    this.bookService.getBooksByAuthorAndYear(this.selectedAuthor, newVal).subscribe(
      books => this.books = books,
      error => this.errorMessage = <any>error
    );
  }

}
